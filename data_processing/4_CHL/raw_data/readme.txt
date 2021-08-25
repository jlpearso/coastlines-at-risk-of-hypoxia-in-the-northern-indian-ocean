Last Updated: 12/29/2020 by Jenna Pearson
====================================================================================================================
Datset Desciption:
--------------------------------------------------------------------------------------------------------------------
This folder contains OC-CCI merged, global satellite monthly chlorophyll-a (chl-a) concentrations. Note that chl-a data are only available over cloud and ice free areas. A blended chl-a estimate from multiple algorithms is provided, where blending is based on the suitability of each candidate algorithm to the optical typology of a given pixel. This approach provides the best estimates of global chl-a across a range of water types (i.e. coastal versus open ocean).  The files contain merged data from MERIS, MODIS, SeaWIFS, VIIRS, and OLCI, and are Level 3 Mapped with a sinusoidal projection. Maybe have to switch to this download cite in the future using CDASPI: https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-ocean-colour?tab=overview.

Data Version:       5.0 
Temporal Coverage:  September 1997 to December 2020
Spatial Coverage:   Global
Resolution:         0.042° x 0.042° (4km x 4km at the Equator)
Units:              (mg/m^3)

Download Website: 

https://climate.esa.int/en/projects/ocean-colour/data/

Product User Guide: 

https://climate.esa.int/en/projects/ocean-colour/key-documents/

====================================================================================================================
Updating Data:
--------------------------------------------------------------------------------------------------------------------
[1] You will need to create an environment and install the necessary packages. See this page for help: https://researchcomputing.princeton.edu/python. Use the following code, entering 'y' after the prompt.

    $ module load anaconda3
    $ conda create --name data_updates numpy xarray scipy netCDF4

After this is successful you should be able to run the scripts. Make sure the environment name matches what is given above.

[2] Run bash script to obtain new data and concatenate all monthly files into 1 file and add date information: 
    $ bash get_data/wget_and_concat.sh

====================================================================================================================
Notes:
--------------------------------------------------------------------------------------------------------------------
* You do not need to register to download from ESA (included are the standard user info). You can manually set the year to update through in wget_and_concat.sh, otherwise the default is the current year.

* Please change the "Last Updated:..." info at the top of this .txt file to the current information.

* The bash script automatically skips over files already present, so if you need to update any files already present on tigress, you will need to delete them first.

* This should be run on tigressdata. To use on jupyterrc you must run the concat_and_process.py file separately.




