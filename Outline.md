# Outline

Journals:

1. Geoscience and Remote Sensing Society GRSS (https://www.grss-ieee.org/)
2. Remote Sensing Letters (https://www.tandfonline.com/journals/trsl20/about-this-journal#aims-and-scope)

Background research
- Study recent articles in the journal
- Read similar or related topic




Research questions

1. How do the observed and modelled data compare?
2. Which model moe accurately represents the measured results? Why?
3. How do TARTES simulations with Robledano's grain shape compare to spherical and fractal grain shapes? What causes these differences?




# Abstract

- Data
- Study area
- research questions
- Methods
- Main findings



# Introduction and Review of Literature

Case study: analysing data from March 19 2021

Motivation: Validation of field spectroscopy measurements as well as preparation for future field campaigns. 

Purpose: comparing the observed and modelled results for surface spectral reflectance.

Literature review
- Based on different data and different methods. HIghlighting the limitations of previous studies
- More recent articles: 10 years old literature

Novelty: 
- The importance of using hyperspectral data for snow albedo data retrieval
    Typically multi channel data are used for albedo retrieval (e.g. MODIS, ASTER, AVHRR)
- A new grain shape algorithm (Robledanoet al., 2023) used in TARTES



# Methods

- Comparing observed spectral reflectance data and modelled data.

## Observed data
- Field spectrometer data ASD Field spec 4
- AVIRIS-NG Surface Spetral Reflectance


## Modelled data

### ISSIA



### TARTES

Creating a lookup table to account formissing SSA values

1. Run TARTES with SSA values ranging between 0 - 60 m2/kg by increments of 1 m2/kg.


2. Use scaled band area approach, or the NDGSI (Eqs. 1 and 3, respectively, from the following paper:
https://doi.org/10.3389/frsen.2022.1038287). Let's say you use the NDGSI, for example. You'll
calculate that value for each of your 60 modeled TARTES spectra. So now you've got a list of 60
NDGSI values that correspond to your 60 different SSAs. This is your lookup table.


3. calculate the NDGSI from your measured field spectrometer data. Match that to the closest NDGSI
value in the lookup table and "retrieve" the corresponding SSA.




# Results, Discussion, and Conclusions










