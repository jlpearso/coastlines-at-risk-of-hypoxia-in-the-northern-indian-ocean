#!/bin/bash

# this script pulls quarterly updates for WOD in single .nc casts then interpolates to a standard depth grid and concats them
# default is single casts

# dwnld_path="latest" # change this to WODXX for published releases where XX is the year 20XX.

# # ============== do not change below this line ================#

# --------------------------------------------------------------
# set paths and filenames
# --------------------------------------------------------------
# file="get_data/filenames.txt"

# # remove the old latest data so that you can update to the newest (if it exists)
# if [ -d "$dwnld_path" ]; then rm -Rf $dwnld_path; fi

# # make new directory
# mkdir $dwnld_path

# # --------------------------------------------------------------
# # download
# # --------------------------------------------------------------
# while IFS= read -r var # read each filename in as a variable "var"
# do
#   echo "======================================================================"
#   echo "Downloading ${var}"
#   echo "======================================================================"
#   #download
#   wget ${var} -P $dwnld_path # download to OSD, PFL etc subfolder
#   #unzip and uncompress
#   gunzip -r $dwnld_path
#   echo "======================================================================"


# done < "$file"

#concatenate
module load anaconda3
conda activate data_updates

python get_data/concat_and_process.py

conda deactivate
echo "Concatenation complete."
