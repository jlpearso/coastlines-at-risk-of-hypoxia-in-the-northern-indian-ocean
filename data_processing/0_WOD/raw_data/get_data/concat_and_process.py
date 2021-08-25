inpath = 'latest/'
outfn = 'all_casts_beginning_to_aug_2020_indian_ocean.nc'
  

###############################################################################################################
# No need to change anything below this line

import xarray as xr
import numpy as np
import pandas as pd
import os
import glob
from tqdm import tqdm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
today = datetime.today()
end_year = today.year

outfn = 'concatenated/' + outfn

file = open("log.txt","w",1) 
file.writelines('File: ' + outfn + ', Processing Date: ' + today.strftime("%m/%d/%Y") + '\n')

# get all the datafiles
fns = glob.glob(inpath + '*.nc')

# can uncomment below to get full range of depth - I choose to cut it off at 2000
# see https://www.ncei.noaa.gov/access/world-ocean-database-select/depth_definition.html
# for depth definitions 
DEPTH = np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,
                 125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,
                 550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,
                 1350,1400,1450,1500])
# loop through to get the total number of profiles for variable initialization
no_profs = 0
for ff,fn in enumerate(fns):
    
    ds_in = xr.open_dataset(fn)
    no_profs = no_profs + len(ds_in.casts)
    

# set up figure for plotting profiles
fig = plt.figure(figsize=(16,10),dpi=200)
ax1 = fig.add_subplot(231)
ax1.set_title('Temperature Profiles')
ax1.set_ylabel('Depth (m)')
ax2 = fig.add_subplot(232)
ax2.set_title('Salinity Profiles')
ax3 = fig.add_subplot(233)
ax3.set_title('Oxygen Profiles')
ax4 = fig.add_subplot(234)
ax4.set_title('Nitrate Profiles')
ax4.set_ylabel('Depth (m)')
ax5 = fig.add_subplot(235)
ax5.set_title('Phosphate Profiles')
ax6 = fig.add_subplot(236)
ax6.set_title('Profile Locations')


# initialize vars
lat = []
lon = []
t = []
cast_id = []
TEMP = np.full([no_profs,len(DEPTH)],np.nan)
DOXY = np.full([no_profs,len(DEPTH)],np.nan)
SAL = np.full([no_profs,len(DEPTH)],np.nan)
NITRATE = np.full([no_profs,len(DEPTH)],np.nan)
PHOSPHATE = np.full([no_profs,len(DEPTH)],np.nan)

varlist = ['OSD','CTD','DRB','MRB','PFL','XBT','MBT','UOR','APB','GLD','SUR']
# varlist = ['OSD']

pr = 0 # set profile counter to 0 and add 1 for each loop

# loop through all datatypes APB, CTD, DRB, MRB, OSD, PFL, XBT
for vv, var in enumerate(varlist):

    fns = sorted(glob.glob(inpath + '*' + var + '*.nc'))
    
    # loop through all files of the same dataset
    for fn in fns:
        # add files to log file to keep track of progress if VPN closes while processing
        file.writelines('Processing: ' + fn + '\n') 

        # read in file
        ds_in = xr.open_dataset(fn)
        
        # for some reason it needs the cc:cc+1 instead of cc but it's the same thing.
        lat.extend(np.array(ds_in.lat))
        lon.extend(np.array(ds_in.lon))
        t.extend(np.array(ds_in.time))
        cast_id.extend([var + '_' + str(s) for s in list(np.array(ds_in.wod_unique_cast))])

        # initialize counters
        temp_row_count = 0
        sal_row_count = 0
        doxy_row_count = 0
        nitrate_row_count = 0
        phosphate_row_count = 0
        z_row_count = 0

        # loop through all casts and extract profiles
        for cc in tqdm(range(len(ds_in.casts)), position=0, leave=True, desc = 'Processing: ' + fn):
#         for cc in tqdm(range(30), position=0, leave=True, desc = 'Processing: ' + fn):

            # find the number of depths in the current cast cc
            z_sz = ds_in.z_row_size[cc]

            if ~np.isnan(z_sz): # no profile available for any variable if nan (this happens sometimes)

                # find the number of temp obs in the current cast profile
                
                if "Temperature" in ds_in:
                    t_sz = ds_in.Temperature_row_size[cc]
                if "Salinity" in ds_in:
                    s_sz = ds_in.Salinity_row_size[cc]
                if "Oxygen" in ds_in:
                    d_sz = ds_in.Oxygen_row_size[cc]
                if "Nitrate" in ds_in:
                    n_sz = ds_in.Nitrate_row_size[cc]
                if "Phosphate" in ds_in:
                    p_sz = ds_in.Phosphate_row_size[cc]


                # get current depth
                z = ds_in.z[z_row_count:z_row_count + int(z_sz)]

                # find the indx of the current z values that are elements of DEPTH
                z_ind = [i for i, val in enumerate(DEPTH) if val in set(np.array(z))]

                # --------------------------------------------------------------
                # TEMP
                # --------------------------------------------------------------
                if "Temperature" in ds_in:
                    # no profile available if nan and flag == 0 --> accepted profile
                    t_sz = ds_in.Temperature_row_size[cc]
                    if (~np.isnan(t_sz)) & (ds_in.Temperature_WODprofileflag[cc] == 0): 
                        if ~np.isnan(t_sz): 
                            # extract cast
                            temp = ds_in.Temperature[temp_row_count:temp_row_count + int(t_sz)]
                            TEMP[pr,z_ind] = temp[z_ind]
                            ax1.plot(TEMP[pr,:],-1*DEPTH)

                # --------------------------------------------------------------
                # Salinity
                # --------------------------------------------------------------
                if "Salinity" in ds_in:
                    # no profile available if nan and flag == 0 --> accepted profile
                    s_sz = ds_in.Salinity_row_size[cc]
                    if (~np.isnan(s_sz)) & (ds_in.Salinity_WODprofileflag[cc] == 0):
                        if ~np.isnan(s_sz):
                            # extract cast
                            sal = ds_in.Salinity[sal_row_count:sal_row_count + int(s_sz)]
                            SAL[pr,z_ind] = sal[z_ind]
                            ax2.plot(SAL[pr,:],-1*DEPTH)


                # --------------------------------------------------------------
                # DOXY
                # --------------------------------------------------------------
                if "Oxygen" in ds_in:
                    # no profile available if nan and flag == 0 --> accepted profile
                    d_sz = ds_in.Oxygen_row_size[cc]
                    if (~np.isnan(d_sz)) & (ds_in.Oxygen_WODprofileflag[cc] == 0): 
                        if ~np.isnan(d_sz):
                            # extract cast
                            doxy= ds_in.Oxygen[doxy_row_count:doxy_row_count + int(d_sz)]
                            DOXY[pr,z_ind] = doxy[z_ind]
                            ax3.plot(DOXY[pr,:],-1*DEPTH)

                # --------------------------------------------------------------
                # NITRATE
                # --------------------------------------------------------------
                if "Nitrate" in ds_in:
                    # no profile available if nan and flag == 0 --> accepted profile
                    n_sz = ds_in.Nitrate_row_size[cc]
                    if (~np.isnan(n_sz)) & (ds_in.Nitrate_WODprofileflag[cc] == 0): 
                        if ~np.isnan(n_sz): 
                            # extract cast
                            nitrate = ds_in.Nitrate[nitrate_row_count:nitrate_row_count + int(n_sz)]
                            NITRATE[pr,z_ind] = nitrate[z_ind]
                            ax4.plot(NITRATE[pr,:],-1*DEPTH)

                # --------------------------------------------------------------
                # PHOSPHATE
                # --------------------------------------------------------------
                if "Phosphate" in ds_in:
                    # no profile available if nan and flag == 0 --> accepted profile
                    p_sz = ds_in.Phosphate_row_size[cc]
                    if (~np.isnan(p_sz)) & (ds_in.Phosphate_WODprofileflag[cc] == 0): 
                        if ~np.isnan(p_sz): 
                            # extract cast
                            phosphate = ds_in.Phosphate[phosphate_row_count:phosphate_row_count + int(p_sz)]
                            PHOSPHATE[pr,z_ind] = phosphate[z_ind]
                            ax5.plot(PHOSPHATE[pr,:],-1*DEPTH) 

                pr = pr + 1
                        
                # move index up
                if "Temperature" in ds_in:
                    if (~np.isnan(t_sz)):
                        temp_row_count = temp_row_count + int(t_sz)
                if "Salinity" in ds_in:
                    if (~np.isnan(s_sz)):
                        sal_row_count = sal_row_count + int(s_sz)
                if "Oxygen" in ds_in:
                    if (~np.isnan(d_sz)):
                        doxy_row_count = doxy_row_count + int(d_sz)
                if "Nitrate" in ds_in:
                    if (~np.isnan(n_sz)):
                        nitrate_row_count = nitrate_row_count + int(n_sz)
                if "Phosphate" in ds_in:
                    if (~np.isnan(p_sz)):
                        phosphate_row_count = phosphate_row_count + int(p_sz)

file.close()
ax6.scatter(lon,lat)
print('Saving Figure...')
plt.savefig(outfn[:-3], dpi=300, bbox_inches='tight')

print('Saving Data...')
# convert to xarray dataset
ds_out=xr.Dataset(
                    coords={'cast': np.arange(no_profs),
                      'depth': DEPTH},
                    attrs = {
                        'date_created': today.strftime("%m/%d/%Y"),
                        'unmerged_data_url': 'https://www.ncei.noaa.gov/access/world-ocean-database-select/dbsearch.html',
                        'geospatial_lat_extent': 'decimal degrees north ' + '(' + str(np.min(lat)) + ',' + str(np.max(lat)) + ')',
                        'geospatial_lon_extent': 'decimal degrees east ' + '(' + str(np.min(lon)) + ',' + str(np.max(lon)) + ')',
                        'help_email': 'OCLhelp@noaa.gov',
                        'history': 'Merged ../latest/*.nc',
                    }
                 )

# add variables to dataset
ds_out["time"]=xr.DataArray(t, dims = ['cast'], coords =[np.arange(no_profs)])
ds_out["lat"]=xr.DataArray(lat, dims = ['cast'], coords =[np.arange(no_profs)])
ds_out["lon"]=xr.DataArray(lon, dims = ['cast'], coords =[np.arange(no_profs)])
ds_out["cast_id"]=xr.DataArray(cast_id, dims = ['cast'], coords =[np.arange(no_profs)])

ds_out["temp"]=xr.DataArray(TEMP, dims = ['cast','depth'], coords =[np.arange(no_profs),DEPTH])
ds_out["sal"]=xr.DataArray(SAL, dims = ['cast','depth'], coords =[np.arange(no_profs),DEPTH])
ds_out["doxy"]=xr.DataArray(DOXY, dims = ['cast','depth'], coords =[np.arange(no_profs),DEPTH])
ds_out["nitrate"]=xr.DataArray(NITRATE, dims = ['cast','depth'], coords =[np.arange(no_profs),DEPTH])
ds_out["phosphate"]=xr.DataArray(PHOSPHATE, dims = ['cast','depth'], coords =[np.arange(no_profs),DEPTH])

# delete if already present
if os.path.isfile(outfn):
    os.remove(outfn)

ds_out.to_netcdf(outfn,mode='w',format = "NETCDF4")
ds_out
