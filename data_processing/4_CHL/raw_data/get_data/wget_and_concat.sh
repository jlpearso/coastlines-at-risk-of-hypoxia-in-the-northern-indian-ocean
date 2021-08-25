#!/usr/bin/bash

end_year="$(date +'%Y')"

# #============== do not change below this line ================#

echo "Updating data through $end_year ..."
echo "======================================================================================"

# user info
usrn=oc-cci-data
pwd=ELaiWai8ae  # this is a public username and pwd for the data

#--------------------------------------------------------------
# set paths and filenames
#--------------------------------------------------------------
dwnld_path='../individual'

#--------------------------------------------------------------
# ftp download only new data files
#--------------------------------------------------------------

mc=9;
for ((n=1997; n<=$end_year; n++));do
     for ((m=1; m<=12; m++));do
         if [ "$m" -le "$mc" ];then
            mon="0${m}"
         else
            mon="${m}"
         fi
         year="${n}"
         
         fname="ESACCI-OC-L3S-CHLOR_A-MERGED-1M_MONTHLY_4km_GEO_PML_OCx-$year$mon-fv5.0.nc"

         if [ -f "$dwnld_path/$fname" ]; then
            echo "$fname exists, skipping download."
         else 
            echo "Downloading $fname"
            echo "======================================================================================"
            webs="ftp://oc-cci-data:ELaiWai8ae@oceancolour.org/occci-v5.0/geographic/netcdf/monthly/chlor_a/"$year"/ESACCI-OC-L3S-CHLOR_A-MERGED-1M_MONTHLY_4km_GEO_PML_OCx-"$year$mon"-fv5.0.nc"
            echo "Didn't skip $dwnld_path/$fname"
            wget --user=$usrn --password=$pwd $webs -P $dwnld_path
            echo "======================================================================================"
         fi
     done
done

echo "Downloads complete."

#--------------------------------------------------------------
# concatenate into one file
#--------------------------------------------------------------

module load anaconda3
conda activate data_updates

python get_data/concat_and_process.py

conda deactivate
echo "Concatenation complete."