# coastlines-at-risk-of-hypoxia-in-the-northern-indian-ocean

## Data Processing Scripts

1. process_wod - initial processing of raw World Ocean Database profiles
2. process_sla - initial processing of raw sea-level anomalies
3. process_chl - initial processing of raw chlorophyll-a
4. regrid_chl_to_sla -  regrids chlorphyll-a data to sea-level anomaly data, must be ran after process_chl and process_sla
5. regrid_sla_to_wod - regrids sea-level anomaly data to World Oean Database profiles, must be ran after process_sla and process_wod

## Figure Making Scripts
1. domain - Makes Fig 1. 
2. hypoxia - Makes Fig 2.
3. sla - Makes Fig 3., Makes Figs. SX-SX (neutral and dmi)
4. chl - Makes Fig 4.
5. risk - Makes Fig. 5
6. cdfs_and_pdfs - Makes Figs. SX-SX
7. correlations - Makes Figs. SX-SX
9. obs_distributions - Makes Figs. SX-SX

## Supplemental

1. make_coastal_mask - creates the coastal mask for data
2. local_functions - file with custom functions - trim this down to only the essential functions
3. pars - sets up global parameters
4. pkgs - imports necessary packages
