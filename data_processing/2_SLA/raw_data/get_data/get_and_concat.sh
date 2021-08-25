#!/usr/bin/bash

end_year="$(date +'%Y')"

# #============== do not change below this line ================#
echo "======================================================================================"
echo "Updating data through $end_year ..."
echo "======================================================================================"

module load anaconda3
conda activate data_updates

echo "Downloading data ..."
echo "======================================================================================"


python get_data/cdaspi_data_request.py

echo "======================================================================================"
echo "Download complete." 
echo "Concatenating data ..."
echo "======================================================================================"

python get_data/concat.py

# too many for cdo so switched to pythonn
# module load cdo
# cdo copy -select,name=sla individual/*.nc all_dt_global_twosat_phy_l4__vDT2018_1993_01_01_to_2020_06_03.nc

echo "Concatenation complete."
echo "======================================================================================"
conda deactivate