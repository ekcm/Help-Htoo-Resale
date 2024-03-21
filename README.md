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

I've created a slide deck to pen down my thought process, check it out [here](https://www.canva.com/design/DAGAHgiXO18/e7TRBIXsLX0qsAwHVO-7hQ/edit?utm_content=DAGAHgiXO18&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)!

<!-- Project Structure -->
## Project Directory Structure
```

|── archive   <- consists of previous iterations of the project housed in jupyter notebooks
|── frontend  <- consists of frontend assets for a simple web application to try out the project
|── model     <- houses all the regression models and cluster coordinates
|── main.py   <- backend entry point to the project.
|                It retrieves the appropriate pickle files from the model folder based on the information given from the frontend
|── tableau   <- consists of tableau files used for exploratory data analysis
|── .ipynb    <- jupyter notebooks ordered by logical order of progress
```

<!-- Starting the project -->
## Starting the project
Run main.py first
```
python main.py
```

cd into frontend, and run 
```
npm run dev
```

<!-- What I learnt -->
## What I Learnt 
1. This was my first time doing a machine learning project, and hence to go from data extraction and cleaning, to EDA, to building the model was difficult and required a lot of reading from different sources and youtube channels.
2. The original idea was to use a single regression model across all the flats in Singapore. But after performing my initial regression model, and looking at the insights from the EDA again, I realized that I could also cluster not just my sector code, but also my coordinates using KMeans clustering, to provide a more accurate model.

<!-- To do -->
## To do
1. Explore other clustering methods such as DBSCAN and Hierarchical-based clustering to further understand the tradeoffs between each clustering model


