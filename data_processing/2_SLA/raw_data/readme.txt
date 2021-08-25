Last Updated: 01/20/2021 by Jenna Pearson
====================================================================================================================
Datset Desciption:
--------------------------------------------------------------------------------------------------------------------
This folder contains merged, global satellite daily absolute dynamic topography and sea level anomaly data at 25km resolution from 1993 onwards where adt = sla + mdt, and mdt is the mean dynamic topography: the twenty year 1993-2012 mean of adt. The files contain merged data from Jason-3, Sentinel-3A, HY-2A, Saral/AltiKa, Cryosat-2, Jason-2, Jason-1, T/P, ENVISAT, GFO, ERS1/2, and are Level 4 Mapped with a ? projection.

Units: (m)

--------------------------------------------------------------------------------------------------------------------
Resources:
--------------------------------------------------------------------------------------------------------------------
Download Website : https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-sea-level-global?tab=form

Documentation    : https://resources.marine.copernicus.eu/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047 

User Guide       : http://marine.copernicus.eu/documents/PUM/CMEMS-SL-PUM-008-032-062.pdf

====================================================================================================================
Updating Data:
--------------------------------------------------------------------------------------------------------------------
From within the get-data directory:

[1] Run bash script to obtain new data and concatenate all monthly files into 1 file and add date information: 
        bash get_data/get_and_concat.sh
    

* If updates are needed for this dataset, and the account information in wget_and_concat.sh does not work, you may register for an  account....





