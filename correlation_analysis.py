#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy.spatial import cKDTree

def rainfall_at_landslides(ls_x, ls_y, xi, yi, zi):
    ls_points = np.column_stack((ls_x, ls_y))
    grid_points = np.column_stack((xi.ravel(), yi.ravel()))

    tree = cKDTree(grid_points)
    dist, idx = tree.query(ls_points, k=1)

    rain_ls = zi.ravel()[idx]

    print("Rainfall at landslide points:")
    print(rain_ls)

    print("Mean rainfall at landslides:", np.mean(rain_ls))
    print("Max rainfall at landslides:", np.max(rain_ls))
    print("Min rainfall at landslides:", np.min(rain_ls))

    return rain_ls

def compute_bins(zi, rain_ls):
    bins = np.linspace(np.nanmin(zi), np.nanmax(zi), 15)
    bin_indices = np.digitize(rain_ls, bins)

    counts = []
    bin_centers = []

    for i in range(1, len(bins)):
        count = np.sum(bin_indices == i)
        counts.append(count)
        bin_centers.append((bins[i] + bins[i-1]) / 2)

    counts = np.array(counts)
    bin_centers = np.array(bin_centers)

    density = counts / np.sum(counts)

    return bin_centers, density

