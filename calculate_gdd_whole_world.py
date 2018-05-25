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

    sea_mask = get_land_sea_mask(land_sea_fname)

    theshold = 37.0
    st_yr = 1970
    en_yr = 2010
    nyears = (en_yr - st_yr) + 1
    nrows = 360
    ncols = 720
    gdd = np.zeros((nrows,ncols))

    yr_cnt = 0
    for year in range(st_yr, en_yr+1):
        print(year)

        fname = os.path.join(met_dir, "GSWP3.BC.Tair.3hrMap.%d.nc" % (year))
        tair, time_steps = open_file(fname)

        for i in range(0, time_steps, 8):
            # Figure out the hottest temperature in the day, the data is 3hrly
            tmax = tair[i:i+8,:,:].max(axis=0)
            gdd += np.where(tmax > theshold, tmax - theshold, 0.0)

        yr_cnt += 1

    #gdd = gdd.mean(axis=0)
    gdd /= float(yr_cnt)
    gdd = np.where(sea_mask == 0, gdd, -999.9)

    ofile = open(os.path.join(odir, "gdd_world.bin"), "w")
    gdd.tofile(ofile)

def get_land_sea_mask(fname):
    nrows = 360
    ncols = 720
    data = np.fromfile(fname, dtype=np.int16).reshape(nrows, ncols)

    return data

def open_file(fname, var="Tair"):
    DEG_2_KELVIN = 273.15

    ds = xr.open_dataset(fname)
    data = ds[var]

    time_steps, nrows, ncols = data.shape
    tair = data.values - DEG_2_KELVIN

    return tair, time_steps


if __name__ == "__main__":

    met_dir = "/Users/mdekauwe/Desktop/Tair"
    #met_dir = "/g/data1/wd9/MetForcing/Global/GSWP3_2017/Tair"

    land_sea_fname = "gswp3_land_sea/world_gswp3_land_sea_mask.bin"

    odir = "outputs"
    if not os.path.exists(odir):
        os.makedirs(odir)

    main(met_dir, odir, land_sea_fname)
