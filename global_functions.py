#===============================================================================================================

# binning for one variable ------------------------------------------------------------#
def latlonbin(invar,lat,lon,bounds,binwidth = 0.25):
    import numpy as np
    import pandas as pd
    
    # create a pandas dataframe
    df = pd.DataFrame(dict(
            invar = np.array(invar),
            lat= np.array(lat),
            lon= np.array(lon),
        ))

    # create 1 degree bins
    latedges = np.arange(bounds[2]-(binwidth/2),bounds[3]+(binwidth/2),binwidth)
    lat_inds = list(range(len(latedges)-1))

    lonedges = np.arange(bounds[0]-(binwidth/2),bounds[1]+(binwidth/2),binwidth)
    lon_inds = list(range(len(lonedges)-1))

    latbins = latedges[1:]-(binwidth/2)
    lonbins = lonedges[1:]-(binwidth/2)

    df['latedges'] = pd.cut(lat, latedges)
    df['lonedges'] = pd.cut(lon, lonedges)
    df['latbins_ind'] = pd.cut(lat, latedges,labels = lat_inds)
    df['lonbins_ind'] = pd.cut(lon, lonedges,labels = lon_inds)
    df['lat_lon_indx']=df.groupby(['latbins_ind', 'lonbins_ind']).ngroup()
    grouped = df.groupby(['latbins_ind', 'lonbins_ind'])

    invar_BINNED = np.zeros((len(latbins),len(lonbins)), dtype=np.ndarray)
    invar_BINNED[:] = np.nan

    invar_binned_ave = np.zeros((len(latbins),len(lonbins)), dtype=np.ndarray)
    invar_binned_ave[:] = np.nan
    
    invar_bincounts = np.zeros((len(latbins),len(lonbins)), dtype=np.ndarray)
    invar_bincounts[:] = np.nan


    #extract the data for each group
    for name, group in grouped:
        i = np.array(group.latbins_ind)
        j = np.array(group.lonbins_ind)

        invar_BINNED[i[0],j[0]] = group.invar

        invar_binned_ave[i[0],j[0]] = np.nanmean(group.invar)   
        
        invar_bincounts[i[0],j[0]] = len(group.invar[np.isfinite(group.invar)]) 

    return np.array(invar_binned_ave,dtype = float),np.array(invar_bincounts,dtype = float),latbins,lonbins

#===============================================================================================================
# mask coastlines ---------------------------------------------------------------------#
def mask_coast(inlat,inlon,inmask,mask_lat, mask_lon):
    import xarray as xr
    import numpy as np
    
    inlat = np.array(inlat)
    inlon = np.array(inlon)
    lat = np.array(mask_lat)
    lon = np.array(mask_lon)
    inmask = np.array(inmask)

    outmask=[]

    for lo,la in zip(inlon,inlat):

        if len(lon[lon<=lo])>0 and len(lat[lat>=la])>0 and len(lon[lon>=lo])>0 and len(lat[lat<=la])>0:
            lon_lim = [lon[lon<=lo][-1],lon[lon>=lo][0]]
            lat_lim = [lat[lat<=la][-1],lat[lat>=la][0]]

            mask_lon = (lon == lon_lim[0]) | (lon == lon_lim[1])
            mask_lat = (lat == lat_lim[0]) | (lat == lat_lim[1])

            mask_tmp = inmask[mask_lat,:]
            mask_tmp = mask_tmp[:,mask_lon]

            outmask.append(np.mean(mask_tmp)>0)
        else:
            outmask.append(False)

    outmask = np.array(outmask)
    
    return outmask
#===============================================================================================================


def o2sat(temp,psal):
    ''' 
        CALCULATE OXYGEN CONCENTRATION AT SATURATION f(T,S)
        
        https://www.mbari.org/products/research-software/matlab-scripts-oceanographic-calculations/
        and python code found here:
        https://github.com/kallisons/pO2_conversion/blob/master/pycode/function_pO2.ipynb
        
        Code is based on: 
        Garcia and Gordon (1992) oxygen solubility in seawater, better fitting equations. L&O 37: 1307-1312
        using the coefficients for umol/kg from the combined fit column of Table 1
      
        Input:   temp = temperature (degree C)
                 sal  = practical salinity (PSS-78)
                 
        Output:  Oxygen staturation at one atmosphere (umol/kg).
        
    '''
    import numpy as np
    
    a_0 =  5.80818;
    a_1 =  3.20684;
    a_2 =  4.11890;
    a_3 =  4.93845;
    a_4 =  1.01567;
    a_5 =  1.41575;
  
    b_0 = -7.01211e-03;
    b_1 = -7.25958e-03;
    b_2 = -7.93334e-03;
    b_3 = -5.54491e-03;
  
    c_0 = -1.32412e-07;
  
    ts = np.log((298.15 - temp) / (273.15 + temp))

    A = a_0 + a_1*ts + a_2*ts**2 + a_3*ts**3 + a_4*ts**4 + a_5*ts**5 
               
    B = psal*(b_0 + b_1*ts + b_2*ts**2 + b_3*ts**3)
               
    O2_sat = np.exp(A + B + c_0*psal**2)
    
    return O2_sat

#===============================================================================================================
def as_si(x, ndp):
    s = '{x:0.{ndp:d}e}'.format(x=x, ndp=ndp)
    m, e = s.split('e')
    return r'{m:s}\times 10^{{{e:d}}}'.format(m=m, e=int(e))

#===============================================================================================================

def add_text(ax, text, x = 0.01, y = .945, fontsize = 12, color = 'k', weight = 'normal', rotation = 0, style = 'normal'):
    ax.annotate(text, xy=(x,y), xycoords="axes fraction", fontsize = fontsize, color = color, style = style,
               weight=weight, rotation = rotation)
    return None

#===============================================================================================================

def add_letter(ax, letter, x = 0.01, y = .945, fontsize = 12, weight='bold', color = 'k'):
    ax.annotate(letter, xy=(x,y), xycoords="axes fraction", fontsize = fontsize, weight='bold', color = color)
    return None

#===============================================================================================================

def ylabel_map(ax,label,x = -0.15, y = 0.5, fontsize = 18, color = 'k'):
    ax.text(x, y, label, va='bottom', ha='center',color = color,
        rotation='vertical', rotation_mode='anchor',
        transform=ax.transAxes, fontsize = fontsize)
    
#===============================================================================================================

def add_single_vert_cbar(fig,p,label, extend = 'neither', loc=[0.925, 0.125, 0.015, 0.75]):
    cbar_ax = fig.add_axes(loc)
    cbar = fig.colorbar(p,cax=cbar_ax, pad=0.04, extend = extend)
    cbar.set_label(label)
    return cbar
    
#===============================================================================================================
def add_land(ax,bounds, countries = False, rivers = False, lakes = False, facecolor = 'w',
             lcolor='dimgray',ccolor = '#878787',rcolor = 'cyan',clw = 0.5):
#             lcolor = '#b5651d',ccolor = '#ca9852',rcolor = '#3944bc'):
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
    import cartopy.feature as cfeature
    land = cfeature.NaturalEarthFeature('physical', 'land', '50m',
                                            edgecolor='face')
    ax.add_feature(land,color=lcolor,zorder = 1) # #b5651d
    ax.background_patch.set_facecolor(facecolor)
#     ax.coastlines(resolution='50m',zorder = 2, color = 'gray)
    if countries == True:
        countries_10m = cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', '10m')
        ax.add_feature(countries_10m,facecolor='None', edgecolor=ccolor, linewidth=0.5) # #65350F
#         ax.add_feature(cfeature.BORDERS)
    if rivers == True:
        rivers_10m = cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '10m')
        ax.add_feature(rivers_10m, facecolor='None', edgecolor=rcolor, linewidth=0.25) # '#404040'
#         ax.add_feature(cfeature.RIVERS)
    if lakes == True:
        ax.add_feature(cfeature.LAKES, alpha=0.5)
    
    g = ax.gridlines(draw_labels=True,alpha=0)
    g.xlabels_top = False
    g.ylabels_right = False
    g.xlabel_style = {'size': 15}
    g.ylabel_style = {'size': 15}
    g.xformatter = LONGITUDE_FORMATTER
    g.yformatter = LATITUDE_FORMATTER
    ax.axes.axis('tight')
    ax.set_extent(bounds, crs=ccrs.PlateCarree())
    ax.outline_patch.set_linewidth(clw)
    return g

#===============================================================================================================

def IOD_year_group_WOD(invar,inlat,inlon,intime,begin,end,IODyears, region = 'none'):
    import numpy as np
    data= []
    lat = []
    lon = []
    time = []
    month = []
    season = []
    for ii,year in enumerate(IODyears):
        start_time = str(year) + begin
        end_time = str(year+1) + end
        time_slice = slice(start_time, end_time)
        
        if region == 'wAS':
            data.extend(np.array(invar.sel(time_wAS=time_slice)))
            lat.extend(np.array(inlat.sel(time_wAS=time_slice)))
            lon.extend(np.array(inlon.sel(time_wAS=time_slice)))
            time.extend(np.array(intime.sel(time_wAS=time_slice)))
            t = intime.sel(time_wAS=time_slice)
            month.extend(np.array(t.dt.month))
            season.extend(np.array(t.dt.season))
        elif region == 'eAS':
            data.extend(np.array(invar.sel(time_eAS=time_slice)))
            lat.extend(np.array(inlat.sel(time_eAS=time_slice)))
            lon.extend(np.array(inlon.sel(time_eAS=time_slice)))
            time.extend(np.array(intime.sel(time_eAS=time_slice)))
            t = intime.sel(time_eAS=time_slice)
            month.extend(np.array(t.dt.month))
            season.extend(np.array(t.dt.season))
        elif region == 'wBoB':
            data.extend(np.array(invar.sel(time_wBoB=time_slice)))
            lat.extend(np.array(inlat.sel(time_wBoB=time_slice)))
            lon.extend(np.array(inlon.sel(time_wBoB=time_slice)))
            time.extend(np.array(intime.sel(time_wBoB=time_slice)))
            t = intime.sel(time_wBoB=time_slice)
            month.extend(np.array(t.dt.month))
            season.extend(np.array(t.dt.season))
        elif region == 'eBoB':
            data.extend(np.array(invar.sel(time_eBoB=time_slice)))
            lat.extend(np.array(inlat.sel(time_eBoB=time_slice)))
            lon.extend(np.array(inlon.sel(time_eBoB=time_slice)))
            time.extend(np.array(intime.sel(time_eBoB=time_slice)))
            t = intime.sel(time_eBoB=time_slice)
            month.extend(np.array(t.dt.month))
            season.extend(np.array(t.dt.season))
        elif region == 'none':
            data.extend(np.array(invar.sel(time=time_slice)))
            lat.extend(np.array(inlat.sel(time=time_slice)))
            lon.extend(np.array(inlon.sel(time=time_slice)))
            time.extend(np.array(intime.sel(time=time_slice)))
            t = intime.sel(time=time_slice)
            month.extend(np.array(t.dt.month))
            season.extend(np.array(t.dt.season))
        
        
    return np.array(data),np.array(lat),np.array(lon),np.array(time),np.array(month),np.array(season)



#===============================================================================================================
def IOD_year_group_grid(invar,begin,end,IODyears, roll = True):
    import numpy as np
    import xarray as xr
    
    data= []
    for ii,year in enumerate(IODyears):
        start_time = str(year) + begin
        end_time = str(year+1) + end
        time_slice = slice(start_time, end_time)
        data.append(invar.sel(time=time_slice))
        
    # add all the data together
    sp_data = xr.concat(data, dim='time')
    # take the mean for each month of all the years
    data = sp_data.groupby('time.month').mean(dim='time')
    #start in June instead of 01
    if roll == True:
        data = data.roll(month=-5,roll_coords = False)
    
    return data, sp_data

#===============================================================================================================

def get_continuous_cmap(hex_list, float_list=None):
    import numpy as np
    import matplotlib.colors as mcolors
    
    ''' creates and returns a color map that can be used in heat map figures.
        If float_list is not provided, colour map graduates linearly between each color in hex_list.
        If float_list is provided, each color in hex_list is mapped to the respective location in float_list. 
        
        Parameters
        ----------
        hex_list: list of hex code strings
        float_list: list of floats between 0 and 1, same length as hex_list. Must start with 0 and end with 1.
        
        Returns
        ----------
        colour map
        
        from here: https://towardsdatascience.com/beautiful-custom-colormaps-with-matplotlib-5bab3d1f0e72
        '''
    rgb_list = [rgb_to_dec(hex_to_rgb(i)) for i in hex_list]
    if float_list:
        pass
    else:
        float_list = list(np.linspace(0,1,len(rgb_list)))
        
    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        col_list = [[float_list[i], rgb_list[i][num], rgb_list[i][num]] for i in range(len(float_list))]
        cdict[col] = col_list
    cmp = mcolors.LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
    return cmp

#===============================================================================================================

def rgb_to_dec(value):
    '''
    Converts rgb to decimal colours (i.e. divides each value by 256)
    value: list (length 3) of RGB values
    Returns: list (length 3) of decimal values'''
    return [v/256 for v in value]

#===============================================================================================================

def hex_to_rgb(value):
    '''
    Converts hex to rgb colours
    value: string of 6 characters representing a hex colour.
    Returns: list length 3 of RGB values'''
    value = value.strip("#") # removes hash symbol if present
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

#===============================================================================================================