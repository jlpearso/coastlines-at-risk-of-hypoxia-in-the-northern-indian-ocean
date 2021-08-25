import xarray as xr
import numpy as np
import os
import glob
from datetime import datetime
today = datetime.today()
end_year = today.year

fns = sorted(glob.glob('/individual/*.nc')) # sorted() makes sure the files are sorted in time

for ff,fn in enumerate(fns):
    print(ff+1, '/', len(fns),  fn)
    
    # read in file
    ds_in = xr.open_dataset(fn)
    
    if ff == 0:
    
        # flip lat from 90 to -90 --> -90 to 90
        lat = np.flipud(ds_in.lat)

        # shift lon from -180 to 180 --> 0 to 360
        lon = np.array(ds_in.lon)
        # set -180 to 0 to be positive 180-360
        lon[lon<0] = lon[lon<0]+360
        #shift forward by half the length to order data 0-360
        lon = np.roll(lon, int(len(lon)/2))
        
        # initialize arrays
        chl = np.full([len(fns),len(lat),len(lon)],np.nan)
        t = []
    
    # get chl and remove time dimension
    chl_a = np.squeeze(np.array(ds_in.chlor_a))
    
    # flip for lat
    chl_a = np.flipud(chl_a)
    
    # shift for lons along rows
    chl_a = np.roll(chl_a, int(len(lon)/2),axis = 1)
    
    # add to variables
    chl[ff,:,:] = chl_a
    t.extend(np.array(ds_in.time))
    
    
# add to xarray dataset
ds_out=xr.Dataset(
                    coords={'time': t,
                      'lat': lat,
                      'lon': lon},
                    attrs = {
                        'date_created': today.strftime("%m/%d/%Y"),
                        'unmerged_data_url': 'https://climate.esa.int/en/projects/ocean-colour/data/',
                        'geospatial_lat_units': 'decimal degrees north (-90,90)',
                        'geospatial_lon_units': 'decimal degrees east (0,360)',
                        'spatial_resolution': ds_in.attrs['spatial_resolution'],
                        'geospatial_lat_resolution': ds_in.attrs['geospatial_lat_resolution'],
                        'geospatial_lon_resolution': ds_in.attrs['geospatial_lon_resolution'],
                        'number_of_bands_used_to_classify': ds_in.attrs['number_of_bands_used_to_classify'],
                        'number_of_optical_water_types': ds_in.attrs['number_of_optical_water_types'],
                        'product_version': ds_in.attrs['product_version'],
                        'processing_level': ds_in.attrs['processing_level'],
                        'sensors': ds_in.attrs['sensor'],
                        'platform': ds_in.attrs['platform'],
                        'product_source': ds_in.attrs['source'],
                        'history': 'Merged ../individual/ESACCI-OC-L3S-CHLOR_A-MERGED-1M_MONTHLY_4km_GEO_PML_OCx-*-fv5.0.nc',
                        'summary': ds_in.attrs['summary']
                    }
                 )

# add variables to dataset
ds_out["chlor_a"]=xr.DataArray(
                    data = chl,
                    dims = ['time','lat','lon'],
                    coords = [t,lat,lon],
                    attrs = {
                        'units': ds_in.chlor_a.attrs['units_nonstandard'],
                        'long_name': ds_in.chlor_a.attrs['long_name'],
                        'parameter_vocab_uri': ds_in.chlor_a.attrs['parameter_vocab_uri']})

outfn = '../concatenated/ESACCI-OC-L3S-CHLOR_A-MERGED-1M_MONTHLY_4km_GEO_PML_OCx-fv5.0_1997_'+str(end_year)+'.nc';
# delete if already present
if os.path.isfile(outfn):
    os.remove(outfn)

ds_out.to_netcdf(outfn,mode='w',format = "NETCDF4")