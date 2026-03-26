#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

def plot_map(xi, yi, zi, boundary_shapes, ls_x, ls_y, xmin, xmax, ymin, ymax):
    fig, ax = plt.subplots(figsize=(8, 6))

    cf = ax.contourf(xi, yi, zi, levels=6, cmap="coolwarm", alpha=0.8)

    for shp in boundary_shapes:
        x, y = zip(*shp.points)
        x = np.array(x)
        y = np.array(y)
        ax.plot(x, y, color="black", linewidth=1.4)

    ls_x_crop, ls_y_crop = [], []
    for x, y in zip(ls_x, ls_y):
        if (y >= ymin) and (x <= xmax):
            ls_x_crop.append(x)
            ls_y_crop.append(y)

    ax.scatter(ls_x_crop, ls_y_crop, color="black", s=15, label="Landslide location")

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    cbar = plt.colorbar(cf, ax=ax, shrink=0.75)
    cbar.set_label("Annual Mean Rainfall (1991-2023)(mm)")

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Rainfall-Induced Landslides in Darjeeling–Soreng region")

    plt.legend()
    plt.tight_layout()

    plt.savefig(
        r"D:\C drive_21-06-2025\Downloads\Downloads_18-02-2026\rain_landslide_masked.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()

def plot_correlation(bin_centers, density, x_smooth, y_smooth, peak_rain, peak_density, model_corr):
    plt.figure(figsize=(6, 4))

    plt.scatter(bin_centers, density, color='blue', label='Observed')

    plt.plot(x_smooth, y_smooth, 'r--', label=f'Quadratic fit (r = {model_corr:.2f})')

    plt.scatter(peak_rain, peak_density, color='black', zorder=5)
    plt.axvline(peak_rain, linestyle='--', color='gray', label=f'Peak Rain={peak_rain:.2f}mm')

    plt.xlabel("Annual Rainfall\n averaged over 1991-2023")
    plt.ylabel("Landslide Density")
    plt.title(f"Rainfall vs Landslide Density\n Darjiling_Soreng region")

    plt.legend()
    plt.grid()
    plt.savefig(
        r"D:\C drive_21-06-2025\Downloads\Downloads_18-02-2026\Annual_rain_landslide_density_correlation.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()

