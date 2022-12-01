#Takes crop as input and returns system scores

take crop as input

fetch dli data for crop input

interpolate data to create functional form

fetch system data

Run raytracing on system at 12 points throughout the day

Numerically integrate (trapezoidal) groundWattage to get daily energy absorbed for each unit area

Convert energy to mols of photons using spectral density

plug in calculated DLI into interpolation to get biomass change with respect to ideal

calculate score to be sum of percent difference between observed and ideal for each unit area

pick systems with highest score

send to variance ranking

