from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import haversine as hs
import pickle
import numpy as np
import requests
import json
import pandas as pd
import os

from numpy import asarray

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def import_dataframes():
  # importing station df
  url = "station_df.csv"
  station_df = pd.read_csv(url)

  # importing mall df
  url = "Mall_df.csv"
  mall_df = pd.read_csv(url)

  return station_df, mall_df

def input_flat_details():
  address = "780A WOODLANDS CRES"
  remaining_months = 1138
  storey = 14
  # address = input("input address here:")
  # remaining_months = int(input("input remaining months here:"))
  # storey = int(input("HDB Flat storey here:"))


  url = "https://www.onemap.gov.sg/api/common/elastic/search?searchVal="+address+"&returnGeom=Y&getAddrDetails=Y&pageNum=1"

  response = requests.request("GET", url)

  query = json.loads(response.text)
  results = query["results"]
  latitude = results[0]["LATITUDE"]
  longitude = results[0]["LONGITUDE"]
  sector_code = results[0]["POSTAL"][:2]

  address_coordinate = (float(latitude), float(longitude))

  return address_coordinate, remaining_months, storey, sector_code, latitude, longitude
   
def get_distance_details(station_df, mall_df, coordinate):

  # distance from nearest MRT Station
  stationLatitudeList = list(station_df['latitude'])
  stationLongitudeList = list(station_df['longitude'])
    
  nearest_station_distance = 99999999
  for i, b in enumerate(stationLatitudeList):
      distance = hs.haversine(coordinate, (float(stationLatitudeList[i]), float(stationLongitudeList[i])))
      if (nearest_station_distance > distance):
          nearest_station_distance = distance
  # print(nearest_station_distance)
  
  # distance from CBD
  distance_from_CBD = hs.haversine(coordinate, (1.28393326234538, 103.851463066212))

  # distance from nearest mall
  mallLatitudeList = list(mall_df['latitude'])
  mallLongitudeList = list(mall_df['longitude'])

  nearest_mall_distance = 99999999 
  for i, b in enumerate(mallLatitudeList):
      distance = hs.haversine(coordinate, (float(mallLatitudeList[i]), float(mallLongitudeList[i])))
      if (nearest_mall_distance > distance):
          nearest_mall_distance = distance
  return nearest_station_distance, distance_from_CBD, nearest_mall_distance

def run_model(sector_code, latitude, longitude, remaining_months, storey, nearest_station_distance, distance_from_CBD, nearest_mall_distance):
# extracting cluster coordinates data from json to compare

  file_path = os.path.join("model", "cluster_coordinates.json")

  with open(file_path, "r") as infile:
      data = json.load(infile)

  cluster_json = json.loads(data)
  sector_cluster_data = cluster_json[str(sector_code)]
  print(sector_cluster_data)

  target_coordinate = [float(latitude), float(longitude)]

  # find the closest cluster
  closest_cluster = None
  min_distance = float('inf')

  for cluster_name, cluster_coordinates in sector_cluster_data.items():
      cluster_x = float(cluster_coordinates[0])
      cluster_y = float(cluster_coordinates[1])
      distance = ((target_coordinate[0] - cluster_x) ** 2 + (target_coordinate[1] - cluster_y) ** 2) ** 0.5
      
      if distance < min_distance:
          min_distance = distance
          closest_cluster = cluster_name

  cluster_num = closest_cluster.split("cluster")[1]

  pickle_file_name = "sector_code_" + sector_code + "_cluster_" + cluster_num + "_model.pkl"

  file_path = os.path.join("model", pickle_file_name)

  with open(file_path, 'rb') as f:
      loaded_model = pickle.load(f)

  X_new = np.array([remaining_months, storey, nearest_station_distance, distance_from_CBD, nearest_mall_distance])
  X_new = X_new.reshape(1, -1)
  y_pred = loaded_model.predict(X_new)

  return y_pred[0]



@app.get("/")
def hello():
    df = import_dataframes()
    flat_details = input_flat_details()
    sector_code = flat_details[3]

    distance_details = get_distance_details(df[0], df[1], flat_details[0])

    numpy_predicted_price_per_sqm = run_model(flat_details[3], flat_details[4], flat_details[5], flat_details[1], flat_details[2], distance_details[0], distance_details[1], distance_details[2])

    predicted_price_per_sqm = numpy_predicted_price_per_sqm.item()
    return dict(predicted_price_per_sqm=predicted_price_per_sqm)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=5000, reload=True)