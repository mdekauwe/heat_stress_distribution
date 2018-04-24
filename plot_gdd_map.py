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

    gdd = np.fromfile(os.path.join(input_dir, "gdd.bin").reshape(nrows, ncols)
    map = np.fromfile(os.path.join(input_dir, "map.bin").reshape(nrows, ncols)

    gdd = np.where(gdd < -9000.0, np.nan, gdd)
    map = np.where(map < -9000.0, np.nan, map)

    plt.imshow(gdd)
    plt.colorbar()
    plt.show()



if __name__ == "__main__":


    input_dir = "outputs"
    main(input_dir)
