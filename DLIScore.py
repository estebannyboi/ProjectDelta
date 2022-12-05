#Takes crop as input and returns system scores

'''
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

'''

import ThermalModel
import numpy as np
from scipy.interpolate import interp1d

def DLIScore(system, APIdata, crop):
    cropParams = cropdata(crop)
    DLIdata = cropParams[1]
    x = DLIdata[0]
    y = DLIdata[1]
    f = interp1d(x,y, kind='cubic')
    score = 0
    DLIvals = thermal(system, APIdata)[1]
    for x in DLIvals:
        for y in DLIvals:
            observed_biomass = f(DLIvals[x][y])
            score += -(observed_biomass - f(cropParams[2]))/(f(cropParams[2]))
    return score

def AbsScore(system, APIdata, crop):
    times = np.linspace(sunrise, sunset, 12) #these times are to be pulled from the APIdata
    score = 0
    for time in times:
        score += Tscore(system, APIdata(time), crop)
    return score

def bestDLIsystems(systems, APIdata, crop):  #systems here will come from TempScores
    amount = len(systems)
    benchmark = round(0.2*amount)
    scores = []
    sysIndexs = []
    for system in systems:
        score = AbsScore(system, APIdata, crop)
        scores.append(score)
        sysIndexs.append([system, score])
    n = benchmark

    scores.sort()
    topTenPercent = scores[-n:]
    finalsystems = []
    for x in sysIndexs:
        if x[1] in topTenPercent:
            finalsystems.append(x[0])

    return finalsystems
