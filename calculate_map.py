#!/usr/bin/env python
# coding: utf-8

"""
Figure out the MAP
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

    sea_mask = get_land_sea_mask(land_sea_fname)

    st_yr = 1970
    en_yr = 2010
    nyears = (en_yr - st_yr) + 1
    nrows = 67
    ncols = 83
    map = np.zeros((nrows,ncols))

    yr_cnt = 0
    for year in range(st_yr, en_yr+1):
        print(year)
        fname = os.path.join(met_dir, "GSWP3.BC.Rainf.3hrMap.%d.nc" % (year))
        rain, time_steps = open_file(fname)
        map += rain.sum(axis=0)
        yr_cnt += 1

    map /= float(yr_cnt)
    map = np.where(sea_mask == 0, map, -999.9)

    ofile = open(os.path.join(odir, "map.bin"), "w")
    map.tofile(ofile)

def get_land_sea_mask(fname):
    nrows = 67
    ncols = 83
    data = np.fromfile(fname, dtype=np.int16).reshape(nrows, ncols)

    return data

def open_file(fname, var="Rainf"):
    mm_s_2_mm_3hr = 60.0 * 60.0 * 3.
    ds = xr.open_dataset(fname)
    data = ds[var]

    # Australia
    lat_st = np.argwhere(data.lat.values == -43.75)[0][0]
    lat_en = np.argwhere(data.lat.values == -10.25)[0][0]
    lon_st = np.argwhere(data.lon.values == 112.75)[0][0]
    lon_en = np.argwhere(data.lon.values == 154.25)[0][0]

    data = data[:,lat_st:lat_en,lon_st:lon_en]
    time_steps, nrows, ncols = data.shape
    rain = data.values * mm_s_2_mm_3hr

    return rain, time_steps


if __name__ == "__main__":

    met_dir = "/Users/mdekauwe/Desktop/Rain"
    #met_dir = "/g/data1/wd9/MetForcing/Global/GSWP3_2017/Tair"

    land_sea_fname = "gswp3_land_sea/australia_gswp3_land_sea_mask.bin"

    odir = "outputs"
    if not os.path.exists(odir):
        os.makedirs(odir)

    main(met_dir, odir, land_sea_fname)
