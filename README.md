# Rainfall-Induced Landslide Analysis (Darjeeling–Soreng Region)

rainfall-landslide-analysis/
│── README.md
│── config.py
│── data_processing.py
│── idw_interpolation.py
│── landslide_density.py
│── correlation_analysis.py
│── plotting.py
│── main.py

## Study Area

Darjeeling–Soreng region (Eastern Himalayas), a landslide-prone mountainous terrain with high rainfall variability.

## Objectives
This project investigates the impact of long-term rainfall patterns over landslide events using gridded IMD rainfall data and observed landslide locations.The region is categorized into different classes, from low to high rainfall regions, using the inverse distance weighting (IDW) interpolation method. 

## Methods

## 1. Data Processing
- IMD gridded rainfall (.nc files)
- Annual rainfall computed by sum over TIME → yearly rainfall
- Multi-year mean calculated

## 2. Spatial Subsetting
- Study region extracted using shapefile boundary
- Additional constraints:
- Latitude ≥ 26.95
- Longitude ≤ 88.35

## 3. IDW Interpolation
Rainfall values are interpolated over a continuous grid using Inverse Distance Weighing (IDW) method. 

## 4. Landslide Rainfall Extraction
- Nearest grid point identified using KDTree
- Rainfall assigned to each landslide location

## 5. Landslide Density Estimation
- Rainfall values grouped into bins
- Landslide Density computed as:
Density = {Landslide events grouped in bins}/{Total landslides}

## 6. Correlation Analysis

- ## Pearson Correlation
  
Measures linear relationship between:
- Rainfall (bin centers)
- Landslide density

- ## 7. Quadratic Model Fit Correlation

- Capture non-linear dynamics
- Identify rainfall peak that represents rainfall level with maximum landslide density


# Outputs

## 1. Rainfall Map
- Interpolated rainfall surface
- Landslide points overlay
- Study boundary visualization

## 2. Correlation Plot
- Landslide density vs rainfall
- Quadratic fit curve
- Peak rainfall threshold
