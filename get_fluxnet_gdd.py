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

    nrows = 360
    ncols = 720

    fname = os.path.join(input_dir, "gdd_world.bin")
    gdd = np.fromfile(fname, dtype=np.float64).reshape(nrows, ncols)

    site = "Casetel d'Assoi"
    row = 264
    col = 24
    print(site, round(gdd[row,col],1))

    site = "Le Bray"
    row = 269
    col = 718
    print(site, round(gdd[row,col],1))

    site = "Mongu"
    row = 149
    col = 46
    print(site, round(gdd[row,col],1))

    site = "Parco Ticino forest"
    row = 270
    col = 18
    print(site, round(gdd[row,col],1))

    site = "Puechabon"
    row = 267 
    col = 7
    print(site, round(gdd[row,col],1))

    site = "Qianyanzhou"
    row = 233
    col = 230
    print(site, round(gdd[row,col],1))

    site = "Roccarespampani"
    row = 264
    col = 23
    print(site, round(gdd[row,col],1))



if __name__ == "__main__":


    input_dir = "outputs"
    main(input_dir)
