#!/usr/bin/env python
# coding: utf-8

"""
Make a land/sea mask for NSW
"""

__author__ = "Martin De Kauwe"
__version__ = "1.0 (06.04.2018)"
__email__ = "mdekauwe@gmail.com"

import os
import sys
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

fname = "gswp3_landmask_nomissing.nc"
ds = xr.open_dataset(fname)
data = ds["landsea"]


data = data.astype(np.int16)
nrows, ncols = data.shape
print(nrows, ncols, nrows*ncols)
data = data.values.reshape(nrows, ncols)
data.tofile("world_gswp3_land_sea_mask.bin")
