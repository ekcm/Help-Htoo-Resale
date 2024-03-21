# Help Htoo Resale

<div id="top"></div>

<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">Help Htoo Resale</h3>

  <p align="center">
    Machine Learning Project to predict HDB Resale Prices
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project was built to help bring more transparency on the real estate market by giving both buyers and sellers an estimate on the fair value of a flat. On the buyer's end, this also helps to tackle the issue with information asymmetry, who can only estimate the market value of the flat based on information provided by the seller and their own assessment of the flat and its surrounding amenities.

<!-- Process -->
## Process

This repository is split into 3 juypter notebooks and 1 Tableau file. 
01. Data Cleaning
* **Data Extraction and Cleaning:** 2017 to 2022 Housing data was obtained from HDB website (https://data.gov.sg/dataset/resale-flat-prices) in December 2022. Data was first cleaned and price was adjusted for inflation.
* **Feature Creation:** Using OneMap API (https://www.onemap.gov.sg/docs/), new features for each individual flat such as coordinate data, postal code, and distances from places of interest such as Central Business District (CBD), MRT Stations, and malls were appended to the dataset
* **Exploratory Data Analysis:** Exploratory Data Analysis was conducted using Tableau (EDA.twb) to better understand the characteristics of the data and unearth important insights and patterns. The main insight we noticed was that each region had its own unique characteristics, which suggests that applying the same regression model on the each flat will lead to a less accurate result, hence the need to first cluster the data before applying the regression model.
![image](https://github.com/ekcm/Help-Htoo-Resale/assets/86366443/31e6ac03-ff83-413c-9804-7af1a87b459e)

02. Clustering with Sector Code
* **Feature Selection:** Features were selected based on highest correlation with the target variable "adjusted_price_per_sqm".
![image](https://github.com/ekcm/Help-Htoo-Resale/assets/86366443/7c4381ba-8423-4bda-8682-a8acd13bf873)
Features selected are: "remaining_months", "storey_avg", "nearest_station_distance", "distance_from_CBD", "nearest_mall_distance". As expected, remaining months on the 99-year HDB flat lease and HDB flat storey have the highest positive correlation with adjusted price per sqm. Distance away from CBD and distance away from the nearest mall are also important features that affect the valuation of the HDB flat lease, as there is a negative correlation, which suggests the further away the HDB flat is from a mall, the lower the value of the HDB flat.
* **Clustering:** The original idea was to use sector codes (first 2 digits of postal codes) to cluster. But even within each sector code, the data could be clustered further, and hence used KMeans to cluster the data by coordinates to provide more granularity.
![image](https://github.com/ekcm/Help-Htoo-Resale/assets/86366443/453967e4-e349-4a34-905b-4fc654bc6ca8)

* **One-hot Encoding:** One hot encoding (One-hot encoding.ipynb) was initially carried out to represent categorical variables as numerical values. However, none of the features selected needed one-hot encoding.

03. Regression with Sector Code
* **Checked for multicollinearity:** Used Variance Inflation Factor (VIF) to check for multicollinearity to ensure independent variables are not highly correlated to each other, as it will cause overfitting.
* **Regression methods:** Compared different Regression methods (Linear Regression, XGBoost Regressor, Random Forest Regressor, KNeighbours Regressor) and identified the best model was XGBoost Regressor, and clustering had a significant impact in improving the quality of the model. Cross-validation is performed to ensure our model is not overfitted.

<!-- What I learnt -->
## What I Learnt 
1. This was my first time doing a machine learning project, and hence to go from data extraction and cleaning, to EDA, to building the model was difficult and required a lot of reading from different sources and youtube channels.
2. Depending on the use case, you can "stack" models on top of each other. The original idea was to use a single regression model across all the flats in Singapore. But after performing my initial regression model, and looking at the insights from the EDA again, I realized that I could also cluster the data to provide a more accurate model. 

<!-- To do -->
## To do
1. Explore other clustering methods such as DBSCAN and Hierarchical-based clustering to further understand the tradeoffs between each clustering model
2. Develop a Python FASTAPI web application to provide a user-interface for users to play around with the model.


