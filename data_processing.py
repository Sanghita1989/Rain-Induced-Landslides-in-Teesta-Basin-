#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shapefile
import xarray as xr
import numpy as np

def load_dataset():
    ds = xr.open_dataset(r"D:\D\Ruvision\IMD 1991_2024\IMD 1991_2017\RF25_ind2007_rfp25.nc")
    print(ds)

def read_shapefiles(boundary_fp, landslide_fp):
    boundary_shp = shapefile.Reader(boundary_fp)
    xmin, ymin, xmax, ymax = boundary_shp.bbox
    boundary_shapes = boundary_shp.shapes()

    ls_shp = shapefile.Reader(landslide_fp)
    ls_x, ls_y = [], []
    for s in ls_shp.shapes():
        x, y = s.points[0]
        ls_x.append(x)
        ls_y.append(y)

    return xmin, ymin, xmax, ymax, boundary_shapes, ls_x, ls_y

def process_rainfall(rain_dir):
    annual_rain = []

    for f in sorted(os.listdir(rain_dir)):
        if f.endswith(".nc"):
            ds = xr.open_dataset(os.path.join(rain_dir, f))
            rain = ds["RAINFALL"].sum(dim="TIME")
            annual_rain.append(rain)

    rain_mean = xr.concat(annual_rain, dim="YEAR").mean(dim="YEAR")
    return rain_mean

def subset_region(rain_mean, xmin, xmax, ymin, ymax):
    lat_vals = rain_mean["LATITUDE"].values

    if lat_vals[0] < lat_vals[-1]:
        rain_mean = rain_mean.sel(
            LATITUDE=slice(ymin, ymax),
            LONGITUDE=slice(xmin, xmax)
        )
    else:
        rain_mean = rain_mean.sel(
            LATITUDE=slice(ymax, ymin),
            LONGITUDE=slice(xmin, xmax)
        )

    return rain_mean

def grid_to_points(rain_mean):
    lon2d, lat2d = np.meshgrid(
        rain_mean["LONGITUDE"].values,
        rain_mean["LATITUDE"].values
    )

    vals = rain_mean.values

    points = np.column_stack((lon2d.ravel(), lat2d.ravel()))
    vals = vals.ravel()

    mask = ~np.isnan(vals)
    points = points[mask]
    vals = vals[mask]

    print("Number of rainfall grid points:", len(vals))

    return points, vals

