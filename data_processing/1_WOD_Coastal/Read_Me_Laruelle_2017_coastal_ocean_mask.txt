File from Alizee Roobaert. April 2020.
mask_coastal1 

0.25 degree grid 
lat: latitude in degrees north (89.875°S – 89.875°N with 0.25° resolution)
lon: longitude in degrees east (179.875°W-179.875°E with 0.25° resolution)
fill_value=0

definition:
"Following Laruelle et al. (2013, 2014), the outer limit of the coastal region corresponds approximately to the
shelf break. Estuaries and inland water bodies are not considered in this study, and the total surface area of
the coastal domain is 28 million square kilometers." see roobaert et al 2019

mask_coastal2

0.25 degree grid 
lat: latitude in degrees north (89.875°S – 89.875°N with 0.25° resolution)
lon: longitude in degrees east (179.875°W-179.875°E with 0.25° resolution)
fill_value=0

definition:
global coastal mask that excludes estuaries and inland water bodies while
its outer limit is set 300 km away from the shoreline leading to a total surface area of 77 million km². see Laruelle et al 2017


mask_global_ocean

0.25 degree grid 
lat: latitude in degrees north (89.875°S – 89.875°N with 0.25° resolution)
lon: longitude in degrees east (179.875°W-179.875°E with 0.25° resolution)
fill_value=0

Mask is performed from the Landschutzer et al. product. See https://www.nodc.noaa.gov/cgi-bin/OAS/prd/accession/details/0209633


surface_mask_coastal1

coastal surface area in km²using the mask_coastal1
0.25 degree grid 
lat: latitude in degrees north (89.875°S – 89.875°N with 0.25° resolution)
lon: longitude in degrees east (179.875°W-179.875°E with 0.25° resolution)
fill_value=NaN;

surface_mask_coastal2

coastal surface area in km² using the mask_coastal2
0.25 degree grid 
lat: latitude in degrees north (89.875°S – 89.875°N with 0.25° resolution)
lon: longitude in degrees east (179.875°W-179.875°E with 0.25° resolution)
fill_value=NaN;


surface_mask_global_ocean

global ocean surface area in km² using the mask_global_ocean
0.25 degree grid 
lat: latitude in degrees north (89.875°S – 89.875°N with 0.25° resolution)
lon: longitude in degrees east (179.875°W-179.875°E with 0.25° resolution)
fill_value=NaN;
