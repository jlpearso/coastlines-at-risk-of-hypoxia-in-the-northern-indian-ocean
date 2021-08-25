#!/usr/bin/env python


######################################
#--------------------------------------------------------------
# set paths
#--------------------------------------------------------------
dwnld_path='individual/'

#--------------------------------------------------------------
# packages
#--------------------------------------------------------------

import numpy as np
import os, os.path, sys
import cdsapi
c = cdsapi.Client()
from datetime import datetime
from zipfile import ZipFile

#--------------------------------------------------------------
# Parameters
#--------------------------------------------------------------
today = datetime.today()
end_year = today.year

variable = 'all'

dataset_name = 'satellite-sea-level-global'

product_type = 'monthly_averaged_reanalysis'

years = list(np.arange(1993,end_year+1))

months = ['01','02','03',
          '04','05','06',
          '07','08','09',
          '10','11','12'
        ]

days = [    '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12',
            '13','14','15',
            '16','17','18',
            '19','20','21',
            '22','23','24',
            '25','26','27',
            '28','29','30',
            '31'
        ]

# function
for year in years:
    fname = f'{dwnld_path}sea_level_{variable}_monthly_{year}.zip'
    #check to make sure the file doesn't already exist - only downloads new data
    if os.path.isfile(fname):
        print(str(year) + ' exists, skipping download' + '    ', fname)
    else:
#         print('error')
        print('Downloading ' + str(year) + '    ', fname)
        c.retrieve(
            dataset_name,
            {
                'product_type': product_type,
                'format': 'zip',
                'variable': variable,
                'year': f'{year}',
                'month': months,
                'day':  days,
            },
            fname)  
        
        #unzip newly downloaded files - make sure to leave the old zipped fiels so it doesn't redownload
        zf = ZipFile(fname, 'r')
        zf.extractall(dwnld_path)
        zf.close()

