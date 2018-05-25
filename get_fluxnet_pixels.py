#!/usr/bin/env python
# coding: utf-8

"""
Figure out the distribution of heat stress (GDD above a threshold) and see if
it correlates with places where it is hot
"""

__author__ = "Martin De Kauwe"
__version__ = "1.0 (24.04.2018)"
__email__ = "mdekauwe@gmail.com"

import os
import sys
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def main(met_dir, odir, land_sea_fname):

    year = 1970
    fname = os.path.join(met_dir, "GSWP3.BC.Tair.3hrMap.%d.nc" % (year))
    data = open_file(fname)

    # rounding to nearest ...
    site = "Casetel d'Assoi"
    lat = 42.25
    lon = 12.25

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Le Bray"
    lat = 44.75
    lon = 360.0-0.75 # map is all positive and france is chunked at the end

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Mongu"
    lat = -15.25
    lon = 23.25

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Parco Ticino forest"
    lat = 45.25
    lon = 9.25

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Qianyanzhou"
    lat = 26.75
    lon = 115.25

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Roccarespampani"
    lat = 42.25
    lon = 11.75

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

def get_rows_cols(data, lat, lon):
    row = np.argwhere(data.lat.values == lat)[0][0]
    col = np.argwhere(data.lon.values == lon)[0][0]

    return row, col

def get_land_sea_mask(fname):
    nrows = 67
    ncols = 83
    data = np.fromfile(fname, dtype=np.int16).reshape(nrows, ncols)

    return data

def open_file(fname, var="Tair"):

    ds = xr.open_dataset(fname)
    data = ds[var]

    return data[0,:,:]


if __name__ == "__main__":

    met_dir = "/Users/mdekauwe/Desktop/Tair"
    #met_dir = "/g/data1/wd9/MetForcing/Global/GSWP3_2017/Tair"

    land_sea_fname = "gswp3_land_sea/gswp3_landmask_nomissing"

    odir = "outputs"
    if not os.path.exists(odir):
        os.makedirs(odir)

    main(met_dir, odir, land_sea_fname)
