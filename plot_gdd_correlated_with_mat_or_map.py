#!/usr/bin/env python
# coding: utf-8

"""
Plot correlation between gdd and mat
"""

__author__ = "Martin De Kauwe"
__version__ = "1.0 (24.04.2018)"
__email__ = "mdekauwe@gmail.com"

import os
import sys
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from scipy.stats import linregress

def main(input_dir):

    nrows = 67
    ncols = 83

    fname = os.path.join(input_dir, "gdd.bin")
    gdd = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)
    fname = os.path.join(input_dir, "mat.bin")
    mat = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)
    fname = os.path.join(input_dir, "map.bin")
    map = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)

    gdd = np.where(gdd < -900.0, np.nan, gdd)
    mat = np.where(mat < -900.0, np.nan, mat)
    map = np.where(mat < -900.0, np.nan, map)

    # just plot a certain bit
    gdd = np.where(mat >= 23.0, gdd, np.nan)
    mat = np.where(mat >= 23.0, mat, np.nan)
    map = np.where(mat >= 23.0, map, np.nan)

    width = 14
    height = 5
    fig = plt.figure(figsize=(width, height))
    fig.subplots_adjust(hspace=0.1)
    fig.subplots_adjust(wspace=0.3)
    plt.rcParams['text.usetex'] = False
    plt.rcParams['font.family'] = "sans-serif"
    plt.rcParams['font.sans-serif'] = "Helvetica"
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['font.size'] = 14
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)



    x = mat[~np.isnan(mat)]
    y = gdd[~np.isnan(gdd)]
    slope, intercept, r_value, p_value, std_err = linregress(x,y)

    ax1.plot(x, y, "k.", alpha=0.1)
    ax1.plot(x, intercept+(x*slope), "r-")
    ax1.set_xlabel("MAT")
    ax1.set_ylabel("GDD")

    x = mat[~np.isnan(map)]
    y = gdd[~np.isnan(gdd)]
    slope, intercept, r_value, p_value, std_err = linregress(x,y)

    ax1.plot(x, y, "k.", alpha=0.1)
    ax1.plot(x, intercept+(x*slope), "r-")
    ax1.set_xlabel("MAP")
    ax1.set_ylabel("GDD")
    plt.show()


if __name__ == "__main__":


    input_dir = "outputs"
    main(input_dir)
