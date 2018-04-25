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
    site = "Calperum"
    lat = -34.25
    lon = 140.75

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Cumberland Plains"
    lat = -33.75
    lon = 150.75

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Gingin"
    lat = -31.25
    lon = 115.75

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Great Western Woodlands"
    lat = -30.25
    lon = 120.75

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Tumbarumba"
    lat = -35.75
    lon = 148.25

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Tumbarumba"
    lat = -35.75
    lon = 148.25

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Whroo"
    lat = -36.75
    lon = 145.25

    row, col = get_rows_cols(data, lat, lon)
    lon_match = np.argwhere(data.lon.values == lon)[0][0]
    print(site, row, col)

    site = "Wombat"
    lat = -37.25
    lon = 144.25

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

    # Australia
    lat_st = np.argwhere(data.lat.values == -43.75)[0][0]
    lat_en = np.argwhere(data.lat.values == -10.25)[0][0]
    lon_st = np.argwhere(data.lon.values == 112.75)[0][0]
    lon_en = np.argwhere(data.lon.values == 154.25)[0][0]

    data = data[:,lat_st:lat_en,lon_st:lon_en]

    return data


if __name__ == "__main__":

    met_dir = "/Users/mdekauwe/Desktop/Tair"
    #met_dir = "/g/data1/wd9/MetForcing/Global/GSWP3_2017/Tair"

    land_sea_fname = "gswp3_land_sea/australia_gswp3_land_sea_mask.bin"

    odir = "outputs"
    if not os.path.exists(odir):
        os.makedirs(odir)

    main(met_dir, odir, land_sea_fname)
