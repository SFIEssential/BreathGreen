# About Data
This data folder contains the raw data acquired from Google AirQuality Hackthon and processed `csv`，`osm` files used in our research.

Raw data: [Google Project Air View Dublin](https://insights.sustainability.google/places/ChIJv2RI7foRZ0gRwAKA8azHAAM) from May 2021 to August 2022

OSM data: Generated from [graph_generator.py](../scripts/graph_generator.py)

**edges_dublinbike.csv**

- Dublin road edges for cyclists.

CSV data: 

**polutants_osm_id_avgValues_OrderedFirst_NegtoNaN.csv**
 - Air pollutant value on each road segment with OSMID.

**attr_dublinbike_withoutna.csv**
 - Dublin bike road attributes (air pollutant value), N/A value fully filled. 

**attr_dublinbike_withoutna_normalised.csv**
 - Normalised Dublin bike road attributes (air pollutant value), with N/A value fully filled.

**result_bike_station.csv**
 - Experiment results from O-D pairs on bike stations.

**result_random_points.csv**
 - Experiment results from O-D pairs randomly picked.

**result_each_pollutant.csv**
 - Experiment results from one O-D pair with different pollutants.

**single_with_GPS.csv**
 - Routes based on the experiment results from one O-D pair with different pollutants.



