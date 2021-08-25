# coastlines-at-risk-of-hypoxia-in-the-northern-indian-ocean

To use this code, it is assumed you have downloaded the data present (with a broken soft link) in any 'get_data' folder and given it the correct names. There are sample scripts to download and work with this data available. Folders and jupyter notebooks are all numbered, with signifies the order in which they should be run.

## Data Processing Scripts

  - 0_WOD - initial processing of raw World Ocean Database profiles
  - 1_WOD_Coastal - applies coastal mask to WOD profiles
  - 2_SLA - initial processing of raw sea-level anomalies
  - 3_DMI - initial processing of the Dipole Mode Index 
  - 4_CHL - initial processing of raw chlorophyll-a
  - 5_Hypoxia_Records - contains the hypoxia record dataset, no scripts to run here.
  - 6_Regridding - regrids chlorphyll-a data to sea-level anomaly data and regrids sea-level anomaly data to World Oean Database profiles
 
## Figure Making Scripts
  - Fig_1_domain.ipynb
  - Fig_2_hypoxia_bar_plot.ipynb
  - Fig_3_SLA.ipynb
  - Fig_4_chl_sla_correlation_map.ipynb
  - Fig_5_risk_map.ipynb
  - Supplementary_Information (makes all SI figures) 

## Other
  - global_functions - file with custom functions used by all scripts
  - global_pars - sets up global parameters used by all scripts
  - global_pkgs - imports necessary packages used by all scripts
