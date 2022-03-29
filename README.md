# Wildfire - Learn and Protect with technology #
Wildfire Project - Create solutions in AML, Streamlit, CoreUI, ChakraUI

YouTube Video:
- Predicting Wildfire Hotspots: Combating California wildfire problem with data and AI/ML
  - https://www.youtube.com/watch?v=mlUcDCKSbOs
- Worldwide Wildfire Data Collection: Combating worldwide wildfire problem with data and AI/ML
  - https://youtu.be/Hf04iW-lT-A

## Dataset Source Info ## 
- Wildfire data is collected from two instruments (MODIS and VIIRS):
  - Moderate Resolution Imaging Spectroradiometer (MODIS) aboard the Aqua and Terra satellites, 
  - Visible Infrared Imaging Radiometer Suite (VIIRS) aboard S-NPP and NOAA 20 (formally known as JPSS-1)
- The MODIS data is available from 
  - November 2000 (for Terra) 
  - July 2002 (for Aqua). 
- VIIRS S-NPP 375 m data is available 
  - from January 2012 to the present 
  - VIIRS NOAA-20 375 m data is available from January 2020  

## Dataset creation ##
Create wildfire dataset for any country by your own using NASA MODIS satellite data 
- [Learn how to create dataset](https://github.com/prodramp/wildfire/blob/main/dataset/README.md)


## Wildfire Hotspot Prediction ## 
![Strategy](https://github.com/prodramp/wildfire/blob/main/images/wildfire-hotspot-strategy.png?raw=true)

CA Wildfire Hotspot Visualization
![Hotspot](https://github.com/prodramp/wildfire/blob/main/images/ca-wildfire-hotspot.png?raw=true)


## Streamlit application to visualization wildfire data for any country by year ##
- [Get the App and try it](https://github.com/prodramp/wildfire/tree/main/wildfire-data-streamlit)

## California Wildfire Dataset Zip files (until March 25th 2022) ##
- Train (2000 - 2019) - Total 1071252 records in 12 columns
  - https://github.com/prodramp/wildfire/raw/main/california-data/ca_fire_train.csv.zip
- Validation Dataset (2020 and 2021) - Total 117936 records in 12 columns
  - https://github.com/prodramp/wildfire/raw/main/california-data/ca_fire_valid.csv.zip
- Test Dataset (Jan - March 2022) - Total 14742 records in 12 columns
  - https://github.com/prodramp/wildfire/raw/main/california-data/ca_fire_test.csv.zip


### Resources: ###
- https://medium.com/ibm-data-ai/predicting-australian-wildfires-with-weather-forecast-data-8d1cc983c863
- https://github.com/Call-for-Code/Spot-Challenge-Wildfires
- https://h2o.ai/wildfire/
- https://github.com/h2oai/challenge-wildfires/blob/main/notebook/DataPreparation.ipynb
- https://github.com/mapbox/mapboxgl-jupyter
- https://www.bigendiandata.com/2017-06-27-Mapping_in_Jupyter/
