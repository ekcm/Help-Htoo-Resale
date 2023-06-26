# Help-Htoo-Resale

## Machine Learning Project to predict HDB Resale Prices

2017 to 2022 Housing data was obtained from HDB website (data.gov.sg/dataset/resale-flat-prices) in December 2022. Data was first cleaned and price was adjusted for inflation.

Using OneMap API (https://www.onemap.gov.sg/docs/), we were able to create new features for each individual flat such as coordinate data, postal code, and distances from places of interest such as Central Business District (CBD), MRT Stations, and malls. 

We performed EDA, and realized that each sector code (first 2 digits of postal code) had their unique characteristics that made performing a regression model across Singapore inaccurate. We were able to further cluster the data by coordinates using KMeans Clustering to provide further granularity.

Finally, we compared different Regression methods (Linear Regression, XGBoost Regressor, Random Forest Regressor) and identified the best model was XGBoost Regressor, and clustering had a significant impact in improving the quality of the model. Cross-validation is performed to ensure our model is not overfitted.

To do:
- Explore other clustering methods such as DBSCAN and Hierarchical-based clustering to further understand the tradeoffs between each clustering model
- Build a Python Flask web application to provide a user-interface for users to play around with our model
