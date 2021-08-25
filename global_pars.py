# the time begin and end of which all data are subsetted initially
ts = '1948-01-01'
te = '2020-05-31'

# entire indian ocean boundaries data are subsetted intially
lat_bounds = [-1.5, 33]
lon_bounds = [48.5, 102.5]

# regional indian ocean boundaries: WAS/EAS,WBoB,EBoB
bounds_wAS = [51.125,64,14.5,28]
bounds_eAS = [64,79.75,3,28]
bounds_eAS_SL = [79,83,3,7]  # use this to attach the small bit to the southeast of Sri Lanka to EAS domain
bounds_wBoB = [79,87,10.25,28]
bounds_wBoB_SL = [80,87,7,10] # use this to attach the small bit to the northeast of Sri Lanka to WBoB domain
bounds_eBoB = [87,103,0,28]

# these are for grouping into the IOD years since the effects are 
# not confined to a single year. Start in June of IOD year, and end in May of the following year.
IODyear_begin = '-06-01' # month-day of IOD year
IODyear_end = '-05-31' # month-day of year AFTER IOD year

cm_bounds = [48.5, 102.5,-1.5, 33]   # plotting bounds for maps

hyp_thresh = 61 #umol/kg, the hypoxia threshold used

