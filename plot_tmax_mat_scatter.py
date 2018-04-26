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

    fname = os.path.join(input_dir, "tmax.bin")
    tmax = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)
    fname = os.path.join(input_dir, "mat.bin")
    mat = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)

    tmax = np.where(tmax < -900.0, np.nan, tmax)
    mat = np.where(mat < -900.0, np.nan, mat)

    width = 9
    height = 6
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

    ax1 = fig.add_subplot(111)


    x = mat[~np.isnan(mat)]
    y = tmax[~np.isnan(tmax)]
    

    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    print(r_value, p_value)

    ax1.plot(x, y, "k.", alpha=0.1)
    ax1.plot(x, intercept+(x*slope), "r-")
    ax1.set_xlabel("MAT")
    ax1.set_ylabel("TMAX")
    plt.show()


if __name__ == "__main__":


    input_dir = "outputs"
    main(input_dir)
