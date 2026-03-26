#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy.spatial import cKDTree

def idw(xy, values, xi, power=2):
    tree = cKDTree(xy)
    
    n_points = len(values)
    if n_points == 0:
        raise ValueError("No rainfall points available after cropping!")
    
    k = min(8, n_points)
    
    dist, idx = tree.query(xi, k=k)
    
    if k == 1:
        return values[idx]
    
    dist[dist == 0] = 1e-10
    
    weights = 1.0 / (dist ** power)
    return np.sum(weights * values[idx], axis=1) / np.sum(weights, axis=1)

def create_grid(xmin, xmax, ymin, ymax):
    xi, yi = np.meshgrid(
        np.linspace(xmin, xmax, 350),
        np.linspace(ymin, ymax, 350)
    )
    return xi, yi

