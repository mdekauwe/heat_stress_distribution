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
from scipy.stats import pearsonr

def main(input_dir):

    nrows = 67
    ncols = 83

    fname = os.path.join(input_dir, "gdd.bin")
    gdd = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)

    site = "Calperum"
    row = 19
    col = 56
    print(site, round(gdd[row,col],1))

    site = "Cumberland Plains"
    row = 20
    col = 76
    print(site, round(gdd[row,col],1))

    site = "Gingin"
    row = 25
    col = 6
    print(site, round(gdd[row,col],1))

    site = "Great Western Woodlands"
    row = 27
    col = 16
    print(site, round(gdd[row,col],1))

    site = "Tumbarumba"
    row = 16
    col = 71
    print(site, round(gdd[row,col],1))

    site = "Whroo"
    row = 14
    col = 65
    print(site, round(gdd[row,col],1))

    site = "Wombat"
    row = 13
    col = 63
    print(site, round(gdd[row,col],1))



if __name__ == "__main__":


    input_dir = "outputs"
    main(input_dir)
