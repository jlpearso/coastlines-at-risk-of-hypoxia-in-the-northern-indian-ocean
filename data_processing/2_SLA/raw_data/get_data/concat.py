import xarray as xr
import numpy as np
import os
import glob
from datetime import datetime
today = datetime.today()
end_year = today.year

fns = sorted(glob.glob('individual/*.nc')) # sorted() makes sure the files are sorted in time
for ff,fn in enumerate(fns):
    print(ff+1, '/', len(fns),  fn)
    
    # read in file
    ds_in = xr.open_dataset(fn)
    
    if ff == 0:
        # initialize arrays
        lon = np.array(ds_in.longitude)
        lat = np.array(ds_in.latitude)
        sla = np.full([len(fns),len(lat),len(lon)],np.nan)
        t = []
        startdate = fn[35:43]

    # get chl and remove time dimension
    sla[ff,:,:]  = np.squeeze(np.array(ds_in.sla))
    t.extend(np.array(ds_in.time))
    
    if ff == len(fns)-1:
        enddate = fn[35:43]

# add to xarray dataset
ds_out=xr.Dataset(
                    coords={'time': t,
                      'lat': lat,
                      'lon': lon},
                    attrs = {
                        'date_created': today.strftime("%m/%d/%Y"),
                        'unmerged_data_url': 'https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-sea-level-global?tab=form',
                        'geospatial_lat_units': 'decimal degrees north (-90,90)',
                        'geospatial_lon_units': 'decimal degrees east (0,360)',
                        'geospatial_lat_resolution': ds_in.attrs['geospatial_lat_resolution'],
                        'geospatial_lon_resolution': ds_in.attrs['geospatial_lon_resolution'],
                        'sensors': ds_in.attrs['ssalto_duacs_comment'],
                        'product_version': ds_in.attrs['product_version'],
                        'processing_level': ds_in.attrs['processing_level'],
                        'software_version': ds_in.attrs['software_version'],
                        'platform': ds_in.attrs['platform'],
                        'history': 'Merged individual/*.nc',
                        'summary': ds_in.attrs['summary'] + ' ' + ds_in.attrs['title']
                    }
                 )

# add variables to dataset
ds_out["sla"]=xr.DataArray(
                    data = sla,
                    dims = ['time','lat','lon'],
                    coords = [t,lat,lon],
                    attrs = {
                        'units': ds_in.sla.attrs['units'],
                        'long_name': ds_in.sla.attrs['long_name'],
                        'comment': ds_in.sla.attrs['comment'],
                        'grid_mapping': ds_in.sla.attrs['grid_mapping']})

outfn = 'concatenated/all_dt_global_twosat_phy_l4__vDT2018_' + startdate + '_to_' + enddate +'.nc';
# delete if already present
if os.path.isfile(outfn):
    os.remove(outfn)

ds_out.to_netcdf(outfn,mode='w',format = "NETCDF4")