#!/usr/bin/env python
# coding: utf-8

"""
Plot correlation between gdd and map
"""

__author__ = "Martin De Kauwe"
__version__ = "1.0 (24.04.2018)"
__email__ = "mdekauwe@gmail.com"

import os
import sys
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def main(input_dir):

    nrows = 67
    ncols = 83

    fname = os.path.join(input_dir, "gdd.bin")
    gdd = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)
    fname = os.path.join(input_dir, "map.bin")
    map = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)

    gdd = np.where(gdd < -900.0, np.nan, gdd)
    map = np.where(map < -900.0, np.nan, map)

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

    from mpl_toolkits.axes_grid1 import make_axes_locatable

    ax1.set_title("GDD")
    im1 = ax1.imshow(gdd, interpolation='None')
    divider = make_axes_locatable(ax1)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im1, cax=cax, orientation='vertical')

    ax2.set_title("MAP")
    im2 = ax2.imshow(map, interpolation='None')
    divider = make_axes_locatable(ax2)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im2, cax=cax, orientation='vertical');


    plt.show()



if __name__ == "__main__":


    input_dir = "outputs"
    main(input_dir)
