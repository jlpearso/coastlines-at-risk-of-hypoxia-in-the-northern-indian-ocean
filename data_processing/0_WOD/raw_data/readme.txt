Last Updated: 03/22/2021 by Jenna Pearson
====================================================================================================================
Datset Desciption:
--------------------------------------------------------------------------------------------------------------------
This folder contains World Ocean Database profiles of temperature, salinity, oxygen, phosphate, and nitrate from a large array of instruments for the northern Indian Ocean. In this directory we include the marked updates (e.g. WOD18) as well as the quarterly updates to this data until the next release (i.e. latest = WOD18 + updates to present). A new folder for the marked releases (WODXX) should be created when available. 

Data files are grouped into several categories.

-------------------------------------------------------------------------------------------------------------------
  Acronym |                Full Name                     |              Key Variables Measured
-------------------------------------------------------------------------------------------------------------------
    OSD   =   Ocean Station Data                         : Temp,Sal,O2,NO3,PO4,SiO4,ALK,DIC,pCO2,pH,Chl
    PFL   =   Profiling Float (e.g. Argo, BioArgo) Data  : Temp,Sal,O2,NO3,ph
    CTD   =   Conductivity, Temperature, Depth Data      : Temp,Sal,O2,Chl        
    XBT*  =   Expendable Bathythermograph Data           : Temp
    MBT   =   Mechanical Bathythermograph Data           : Temp
    DRB   =   Drifting Buoy Data                         : Temp,Sal,O2
    MRB   =   Moored Buoy Data                           : Temp,Sal
    APB   =   Autonomous Pinninped Bathythermograph Data : Temp,Sal
    UOR   =   Undulating Ocean Recording Data            : Temp,Sal,O2,Chl
    SUR** =   Surface Only Data                          : Temp,Sal,Chl,ALK,pCO2,ph
    GLD   =   Glider Data                                : Temp,Sal,O2
--------------------------------------------------------------------------------------------------------------------
* The Levitus 2009 XBT correction was applied (it is the only one available for standard depths). 
** SUR variables not inlcuded in the concatenated dataset.
 
Temporal Coverage    :    January 1773 - 2018 published, quarterly updates to present
Spatial Coverage     :    lat_bounds = [-1.5,33], lon_bounds = [48.5,102.5]
Resolution           :    non-uniform spacing
Units                :    Temp (deg C), Sal (unitless), O2/NO3/PO4 (umol/kg)

====================================================================================================================
Resources:
--------------------------------------------------------------------------------------------------------------------
Data Website          :   https://www.nodc.noaa.gov/OC5/WOD/pr_wod.html
Download Website      :   https://www.ncei.noaa.gov/access/world-ocean-database-select/dbsearch.html
Product User Guide    :   https://www.nodc.noaa.gov/OC5/WOD/docwod.html
FAQs                  :   https://www.nodc.noaa.gov/OC5/WOD/wod-woa-faqs.html
Netcdf description    :   https://www.nodc.noaa.gov/OC5/WOD/netcdf_descr.html
Flag Codes            :   https://www.nodc.noaa.gov/OC5/WOD/CODES/Definition_of_Quality_Flags.html
XBT/MBT Corrections   :   https://www.ncei.noaa.gov/access/world-ocean-database-select/xbt_bias_info.html

====================================================================================================================
Getting Updates: Please see the screenshots within latest or WOD18 for help.
--------------------------------------------------------------------------------------------------------------------
[1] Go to https://www.ncei.noaa.gov/access/world-ocean-database-select/dbsearch.html
[2] Do not check any boxes, and click "Build Query".
[3] On the next page, leave all fields as they are (it says you cant exclude data based on flags for .nc files) except add in the lat/lon bounds from above, click in column 1 Temperature, Salinity, Oxygen, Phosphate, Nitrate. 
    - If you are doing a published update (i.e. WODXX where XX is the release year), create an entirely now folder for it by modifying dwnld_path in get_data/wget.sh to be WODXX where XX is the update year. Please change this back to "latest" after.
[4] Click "Get Inventory"
[5] It should give you an estimate of the extraction time at the bottom of the page. Click "Download Data"
[6] Select .... Format:  "ragged array" (netcdf), Depth Level: "standard level data". XBT Correction: "Levitus 2009". Enter your email then click "Extract Data".
[7] Wait for your email with links to the data.
[8] Copy the new list into the get_data/filenames.txt file.
[9] Run bash get_data/wget_and_concat.sh
[10] Make sure the last file has downloaded from your list, otherwise you may need to move the cursor in filenames.txt to the next line
====================================================================================================================
Notes:
--------------------------------------------------------------------------------------------------------------------
* Please change the "Last Updated:..." info at the top of this .txt file to the current information.
*



