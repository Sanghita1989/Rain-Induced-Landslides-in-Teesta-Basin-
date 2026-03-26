#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from config import *
from data_processing import *
from idw_interpolation import *
from landslide_density import *
from correlation_analysis import *
from plotting import *

# Dataset check
load_dataset()

# Read shapefiles
xmin0, ymin0, xmax0, ymax0, boundary_shapes, ls_x, ls_y = read_shapefiles(boundary_fp, landslide_fp)

# Apply cropping override
ymin = 26.95
xmax = 88.35
xmin = xmin0
ymax = ymax0

# Rainfall processing
rain_mean = process_rainfall(rain_dir)
rain_mean = subset_region(rain_mean, xmin, xmax, ymin, ymax)

points, vals = grid_to_points(rain_mean)

# IDW
xi, yi = create_grid(xmin, xmax, ymin, ymax)
interp_points = np.column_stack((xi.ravel(), yi.ravel()))
zi = idw(points, vals, interp_points).reshape(xi.shape)

# Landslide rainfall
rain_ls = rainfall_at_landslides(ls_x, ls_y, xi, yi, zi)

# Density
bin_centers, density = compute_bins(zi, rain_ls)

# Correlation
x_smooth, y_smooth, peak_rain, peak_density, model_corr = correlation_analysis(bin_centers, density)

# Plot
plot_map(xi, yi, zi, boundary_shapes, ls_x, ls_y, xmin, xmax, ymin, ymax)
plot_correlation(bin_centers, density, x_smooth, y_smooth, peak_rain, peak_density, model_corr)

