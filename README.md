# Welcome to the NASA UW Hackweek FMI Project 2024

## The Purpose of the project

The purpose of the project is to validate SnowEX data from March 19 2021. This is achieved by comparing AVIRIS-NG surface spectral reflectance and field spectrometer measurements to simulated results. Multi channel data are commonly used for albedo retrievals, and therefore using hyperspectral AVIRIS-NG data adds novelty to the research. Surface reflectance is modeled with with the Two-streAm Radiative TransfEr in Snow TARTES. A new breakthrough for an approximation for the optical shape of snow is used when modelling with TARTES (Robledano et al., 2023). The grain shape approximation is based on simulating light propagation in three-dimensional images of natural snow at the micrometer scale. The results are compared with more simplified pherical and fractal grain shape approximations. Beyond this, the aim is to simulate the effects of surface roughness on snow albedo with a TARTES reduction (Manninen et al., 2009). In addition, Imaging Spectroscopy Snow and Ice Algorithm ISSIA is used for modelling broadband albedo. 


## What is albedo, and why does it matter?

Albedo α is defined as the ratio of reflected (F↑S) and incoming solar flux (F↑S),
measured on a scale from 0 to 1 (Stephens et al. , 2015). Albedo value of 0 corresponds to
a theoretical black body which absorbs all incident radiation. On the other hand an
albedo value of 1 corresponds to a theoretical body that reflects all incident radiation.


![albedo definition](https://github.com/user-attachments/assets/3e9b83fa-3e3f-46c6-aa59-f1536e675621)


Snow and ice have the highest albedo out of all of the terrain types on Earth. When the global temperature rises, snow and ice melt, leading to a decreased surface albedo. Consequently more radiation will be absorbed. This phenomenon is known as albedo feedback loop. Surface albedo has a considerable effect when considering the planetary energy budget, or the overall balance between the incoming radiation from the sun and the outgoing radiation from the Earth (Thomas, 2017). Monitoring snow albedo on a large-scale requires satellite remote sensing methods. In situ measurements of reflectivity and scattering properties of snow need to be studied in order to study the satellite data. Surface roughness typically decreases snow albedo. Further research on the topic is needed. 


![Global energy balance](https://github.com/user-attachments/assets/22fa794f-a60e-4a87-8c98-998edcc26f26)



Figure 1.1: Visualization of the global energy balance of the Earth. Units for the estimated magnitudes of the globally averaged energy balance components are $$Wm^{-2}$$. The uncertainty ranges are provided in parenthesis. Source: (Wild et al. , 2013)


Spectral surface reflectance on the other hand stands for the ratio of the light reflected as a function of the wavelength. Albedo can be calculated by integrating over the entire solar spectrum. See Figure 1.2 for an exmple of spectral reflectance of different materials. Each material has their characteristic spectral signature. 

![image](https://github.com/user-attachments/assets/4ba4a56d-2100-47e0-b2f5-d74ed8113d3f)

Figure 1.2: Spectral surface reflectance of snow, vegetation, dry soil and water (reflectance vs. wavelength). Source: (Webb, 2024)




# The Two-streAm Radiative TransfEr in Snow TARTES


The Two-streAm Radiative TransfEr in Snow TARTES is a fast and user friendly optical radiative transfer model used to compute bulk spectral albedo of a given snowpack (Libois et al., 2013). TARTES is accurate in the visible and near-infrared range for pristine snow. Impurities can be represented as Raileigh scatters, where their size is assumed much smaller than the wavelength. The model is based on formalism for weakly absorbing media to describe the sinle scatterinf properties of each layer and the delta-Eddington approximation to solve the radiative transfer equation (Kokhanovsky and Zege, 2004). TARTES has been written with Python. It is open source software with GPL License, and can be accessed here: https://github.com/ghislainp/tartes. 

Robledano et al. (2023) provide a new breakthrough for a new approximation for the optical shape of snow. It is based on simulating light propagation in three-dimensional images of natural snow at the micrometer scale. The results are compared with more simplified pherical and fractal grain shape approximations. 




## Snow TARTES

![image](https://github.com/user-attachments/assets/4024b44a-4def-48d2-8d10-aec0fdc7d800)

Figure 1.3: Snow TARTES

Snow TARTES is a web application used to compute the reflection (albedo) from multi-layered snowpack. Snow TARTES represents snowpack as a stack of horizontal homogeneous layers. The input variables include:
- Thickness
- Density
- Specific Surface Area (SSA) is used to describe scattering area per volume
- Grain shape depends on the asymmetry factor g and absorption enhancement parameter B
  	- Robledano et al. 2023, Nature Communications (See article in Materials folder)
  	- Sphere
  	- Fractal
- Anthropogenic and natural impurities (black carbon, dust and snow algae)

Access Snow TARTES here:

https://snow.univ-grenoble-alpes.fr/snowtartes/

Access TARTES documentation here:

https://snow.univ-grenoble-alpes.fr/tartes/docs/tartes.html 



## Creating a lookup table to account for missing SSA values

Run TARTES with SSA values ranging between 0 - 60 m2/kg by increments of 1 m2/kg.

Use scaled band area approach, or the NDGSI (Eqs. 1 and 3, respectively, from the following paper: https://doi.org/10.3389/frsen.2022.1038287). Let's say you use the NDGSI, for example. Calculate that value for each of your 60 modeled TARTES spectra. So now you've got a list of 60 NDGSI values that correspond to your 60 different SSAs. This is the lookup table.

calculate the NDGSI from your measured field spectrometer data. Match that to the closest NDGSI value in the lookup table and "retrieve" the corresponding SSA.



# Adding small-scale surface roughness effects to TARTES


![image](https://github.com/user-attachments/assets/55706396-141e-4883-a2a3-bb12c0dbc12e)

Figure 1.4: Visualization of a possible path involvinf facet-to-facet scattering on a randomly rough surface os spherical scatterers. Source: (Manninen et al., 2009)


Manninen at al. (2009) introduced an additional model that accounts for small scale surface roughness that can be combined with TARTES. The results of Manninen's reduction are subtracted from the modelled TARTES albedo. Manninen et al. found that small-scale surface roughness can decrease surface albedo by up to 0.1. See Figure 1.5 for comparisons between spectral reflectance simulations and results modelled with TARTES. 

![image](https://github.com/user-attachments/assets/4af9d1d2-eae6-4c2a-b930-7ef2e2f97e36)

Figure 1.5: Snow reflectance spectral measured using the ASD spectrometer, and simulated with the TARTES model. Grey variation range shows the ASD spectrometer in Hirviäkuru (67.38◦ N,
26.85◦ E) on 13 March and in Mantovaaranaapa (67.4◦ N, 26.72◦ E) on 22 April 2009. The albedo simulations using the TARTES model are shown
for fractal grains (blue) and spheres (red) Source: (Qu et al., 2015)


## Mathematics behind TARTES extension 


Scattering of light in canopies is described with photon recollision theory, p theory

p = parameter for photon recollision theory
	- spectrally invariant
	- depends on the amount of scattering surface in the volume
	- Is applied to simulate rough snowpack

n = the number of facet-to-facet scattering sequences. f(n) is dominated by values n=0 and n=1. For a single photon, the number of facet-to-facet volume scattering is an integer number

< n > = ensemble of photons



Scattering of direct radiation


For direct radiation, one must take into account that irradiance depends on solar zenith angle, in addition to the wavelength

p1 = first scattering sequence

p = latter scattering sequences


- The first scattering evet depends on solar zenith angle. 

- The following scattering events are assumed to be independent of the solar zenith angle of the original incident radiation

  

The bidirectional reflectance factor BRF, is a ratio between outgoing radiance at one given direction and incoming radiance at another given direction. The impact of surface roughness on albedo increases as solar zenith angle increases. Source: (Zhang et al, 2021)


![image](https://github.com/user-attachments/assets/a2588dd5-fc54-45d7-9d7a-269737774a88)

Figure 1.6: Visualizing surface albedo. The red lines indicate the incident directions and the blue lines indicate the viewing directions. (a) Black-sky albedo (b) White-sky albedo. Blue-sky albedo is a combination of white-sky and black-sky albedo conditions. 




![image](https://github.com/user-attachments/assets/b074c298-5be5-4045-b27d-70c36788c32f)

Figure 1.7: Visualization of Sun Azimuth and Sun Zenith angles (Zhang et al. 2021). 


The impact of surface roughness on albedo increases with the progress of the melting season. When snow is darker, the effect of the roughness may be more pronounced. As snow is melting, impurities cause deep narrow pits to form in the snowpack. They sink in the snowpack as a result of absorption of solar radiation (Manninen et. al). 


![Perovich et al, 2002](https://github.com/user-attachments/assets/32289492-091a-4095-a282-f21f50075983)

Figure 1.8: There are five stages in albedo evolution for the Arctic, which include dry snow, melting snow, pond formation, pond evolution, fall freezeup. The graph shows a time series of wavelength integrated albedo from 1 April 1998 through 27 September 1998, averaged over a 200 m line. The standard deviation of albedo measured along the albedo line is plotted as open circles. Source: (Perovich et al. , 2002)



# ISSIA

ISSIA Imaging Spectrometer - Snow and Ice Algorithm produces retrievals of broadband albedo, optical grain radius, and radiative forcing by light absorbing particles (LAPs) (Donahue et al., 2013). 


INPUTS:

The ATCOR-4 .inn file (this pulls the solar zenith angle for each flight line)
The atmospherically corrected reflectance file (atm.dat)
The modeled global solar flux at the ground (eglo.dat)
The terrain slope map from ATCOR-4 (slp.dat)
The terrain aspect map from ATCOR-4 (asp.dat)

OUTPUT:

A separate geotiff is saved for each retreival in the same directory as the in put files. Pixels with retreival value are stored with a nan. NOTE: The Coordinate reference system code is a required input and is currently set to WGS 84 / UTM Zone 10N for Place Glacier. If processing data elsewhere update coordRefSysCode.


MATLAB script on GitHub:

https://github.com/donahuechristopher/ISSIA


# Study site: Grand Mesa & Senator Beck Basin, Colorado


![image](https://github.com/user-attachments/assets/60354fd4-d7dc-40c4-a0c9-32e938bcc1bb)

Figure 1.9: Study site location in Grand Mesa & Senator Beck Basin, Colorado. The date of spectrometer measurements is 19 March 2021.

The SnowEX21 AVIRIS-NG data set provides apparent surface spectral reflectance imagery which demonstrates snow albedo and snow optical property evolution across two distinct snow-covered environments in Colorado. Data collection occurred in the spring of 2021 as part of the NASA SnowEx mission. The two study sites (Senator Beck Basin and Grand Mesa) were chosen for their contrasting terrain and vegetation characteristics. Data collection occurred over three days (19 March, 1 April, and 29 April) to produce a time series data set across varying snow conditions. 

Senator Beck Basin is a high elevation alpine basin in the San Juan mountains in southwest Colorado. The basin features complex topography and minimal vegetation due to its location above tree line. Grand Mesa is a flat-topped mountain located in west central Colorado. The northwest portion of Grand Mesa selected for this work is relatively flat and well-forested. The three dates selected for data collection
exhibited changing snow conditions through time: 1) cold, clean snow (19 March), 2) warming, clean snow (11 April), and 3) melting, dirty snow (29 April). The date chosen for the data analysis is 19 March 2021.


# Project Tasks

1. Plot field spectrometer data. Choose one instrument. 

2. Model spectral reflectance with Snow TARTES using field station measurements as inputs (https://snowstudies.org/archival-data/). 

3. Plot AVIRIS-NG data. Use tutorial: https://snowex-2024.hackweek.io/tutorials/albedo/aviris-ng-data.html. 

4. Model spectral reflectance with ISSIA. 

5. Make a lookup table for SSA values. 

6. Model spectral reflectance with TARTES with python.

7. Model broadband albedo, optical grain radius, and radiative forcing by light absorbing particles (LAPs).

8. Apply Manninen's reduction to TARTES in order to correct the modelled results for surface roughness. Consider using UAVSAR high-precision elevation data to validate the results. Compare the modeled spectra to the corresponding AVIRIS-NG pixel spectra. Repeat as many times as possible within available time. 

    Hypothesis: Manninen et al. (2009) found that small-scale surface roughness can decrease the total albedo by up to about 0.1. Therefore it can be assumed that the AVRIS reflectance values results should be consistently lower in contrast to the TARTES bulk-modelled albedo.






# Software


## Miniconda

https://docs.anaconda.com/miniconda/#miniconda-latest-installer-links


![image](https://github.com/user-attachments/assets/142469fa-26d1-4ccd-9556-eb7e643e20e1)

## Anaconda

https://www.anaconda.com/installation-success?source=installer


## Virtual Enviroment


Use the following command in the NASA-Hackweek-FMI-Project folder to create a virtual environment in command prompt:

conda env create -f conda-env_NASA_UW_hackweek.yml


## GitHub desktop

Github desktop is a great tool for simplifying the development workflow. 

Download Github desktop here: 

https://desktop.github.com/download/

## Visual Studio Code

Download Visual Studio Code here:

https://code.visualstudio.com/docs/?dv=win64user



## QGIS

Download QGIS here:

https://qgis.org/download/

Instruction for Windows

![image](https://github.com/user-attachments/assets/2a61d948-fa0d-4c26-b50e-6ee079824f44)

Choose the Long Term Version


## Python data module for plotting spectral reflectance data:

Spectral Documentation:

https://www.spectralpython.net/


## Python TARTES module

https://pypi.org/project/tartes/



# SnowEX Data

## SnowEX tutorials

https://snowex-2024.hackweek.io/intro.html

## SnowEX documentation

https://nsidc.org/data/snowex/documents

https://snow.nasa.gov/sites/default/files/users/user354/SNEX-Data/SNEX%20main.pdf

https://nsidc.org/data/search#keywords=snowex21/sortKeys=score,,desc/facetFilters=%257B%257D/pageNumber=1/itemsPerPage=25


## SSA data

Snowpit location in Grand Mesa can be found in NASA-UW-Hackweek-FMI-Project\Earthdata\SSA data\snex21_ts_sp_mean_locations.csv

### SnowEx21 Time Series Snow Pits, Version 1

https://nsidc.org/data/snex21_ts_sp/versions/1

### Earthdata

https://search.earthdata.nasa.gov/search/granules/collection-details?p=C3046987606-NSIDC_ECS&pg%5B0%5D%5Bv%5D=f&pg%5B0%5D%5Bgsk%5D=-start_date&g=G3047676767-NSIDC_ECS&q=SNEX21_TS_SP%20V001&tl=1723956531.382%213%21%21




## SnowEx21 Senator Beck Basin and Grand Mesa, CO AVIRIS-NG Surface Spectral Reflectance


### AVIRIS-NG Surface Spectral Reflectance Tutorial

https://snowex-2024.hackweek.io/tutorials/albedo/aviris-ng-data.html

### Dataset description

https://data.nasa.gov/dataset/SnowEx21-Senator-Beck-Basin-and-Grand-Mesa-CO-AVIR/dnnd-kuv2/about_data

### NSIDC

https://nsidc.org/data/snex21_ssr/versions/1


### Earthdata

https://search.earthdata.nasa.gov/search/granules?p=C2560987849-NSIDC_ECS&pg[0][v]=f&pg[0][gsk]=-start_date&q=SNEX21_SSR%20V001&tl=1723940896.877!3!!

https://search.earthdata.nasa.gov/search?q=SNEX21_SSR%20V001



# UAVSAR data

## UAVSAR Tutorial

https://snowex-2021.hackweek.io/tutorials/sar/uavsar.html#what-is-uavsar

## UAVSAR Repeat Pass Interferometry Scene DEM TIFF

https://data.nasa.gov/dataset/UAVSAR_INSAR_DEM/g2f9-dzjv/about_data

## UAVSAR data search

https://uavsar.jpl.nasa.gov/cgi-bin/data.pl


## UAVSAR-Ka (GLISTIN-A)

UAVSAR-Ka is a state-of-the-art Ka-band airborne single-pass interferometric SAR designed to map land surface topography. It is part of the UAVSAR instrument suite.

https://uavsar.jpl.nasa.gov/technology/ka-band.html






# References:

Donahue, C., Menounos, B., Viner, N., Skiles M., Beffort, S., Denouden, T., Gonzalez Arriola S., White, R., Heathfield, D., Bridging the gap between airborne and spaceborne imaging spectroscopy for mountain glacier surface property retrievals, Remote Sensing of Environment, Volume 299, 2023, 113849, ISSN 0034-4257, https://doi.org/10.1016/j.rse.2023.113849.

Libois, Q., Picard, G., France, J. L., Arnaud, L., Dumont, M., Carmagnola, C. M., and King, M. D.: Influence of grain shape on light penetration in snow, The Cryosphere, 7, 1803–1818, https://doi.org/10.5194/tc-7-1803-2013, 2013.

Manninen, T., Anttila, K., Jääskeläinen, E., Riihelä, A., Peltoniemi, J., Räisänen, P., Lahtinen, P., Siljamo, N., Thölix, L., Meinander, O., Kontu, A., Suokanerva, H., Pirazzini, R., Suomalainen, J., Hakala, T., Kaasalainen, S., Kaartinen, H., Kukko, A., Hautecoeur, O., and Roujean, J.-L.: Effect of small-scale snow surface roughness on snow albedo and reflectance, The Cryosphere, 15, 793–820, https://doi.org/10.5194/tc-15-793-2021, 2021.

Robledano, A., Picard, G., Dumont, M. et al. Unraveling the optical shape of snow. Nat Commun 14, 3955 (2023). https://doi.org/10.1038/s41467-023-39671-3

Stephens, G. L., O’Brien, D., Webster, P. J., Pilewski, P., Kato, S., and Li, J. 2015.
The albedo of Earth. Reviews of Geophysics, 53(1), 141–163.

Thomas, D. N. 2017. Sea ice, third edition. John Wiley and Sons, Incorporated.

Perovich, D. K., Grenfell, T. C., Light, B., and Hobbs, P. V. 2002. Seasonal evolution
of the albedo of multiyear Arctic sea ice. Journal of Geophysical Research: Oceans,
107(C10), SHE 20–1–SHE 20–13.

Qu, Y., Liang, S., Liu, Q., He, T., Liu, S., Li, X. (2015). Mapping Surface Broadband Albedo from Satellite Observations: A Review of Literatures on Algorithms and Products. Remote Sensing. 7. 990-1020. 10.3390/rs70100990. 

Wild, M., Folini, M., Schär C., Loeb N., Ellsworth G. D, and König-Langlo, G. 2013.
The global energy balance from a surface perspective. Climate Dynamics, 40(11),
3107–3134.

Webb, Reflectance Spectra of Materials on Earth’s Surface, webbtelescope.org/contents/media/images/01F8GFAGTM98YTKDS0FZAAWWV2. Accessed 18 Aug. 2024. 

Zhang, Yichao & Wijeratne, Lakitha & Talebi, Shawhin & Lary, David. (2021). Machine Learning for Light Sensor Calibration. Sensors. 21. 6259. 10.3390/s21186259. 


