#Eliminates systems that produce extreme temperatures

'''
take crop as input and find growth temp range

run thermal model at 12 points throughout the day on each system

for each unit area, if temp is in range, give it score of 1, if outside, give it 0

add sum of scores at any point in the day with the rest to produce final score

Highest score (including tied) gets sent to DLIScore function
'''

import thermal
import numpy as np

def Tscore(system, APIdata, crop):
    cropParams = cropdata(crop)
    Trange = cropParams[0] # length 2 list of lower/upper bound
    bottomtemps = thermal(system, APIdata)[0]
    score = 0
    for x in bottomtemps:
        for y in bottomtemps:
            if Trange[0] <= bottomtemps[x][y] <= Trange[1]:
                score += 1
            else:
                score -= 2
    return score

def AbsScore(system, APIdata, crop):
    times = np.linspace(sunrise, sunset, 12) #these times are to be pulled from the APIdata
    score = 0
    for time in times:
        score += Tscore(system, APIdata(time), crop)
    return score

def bestTSystems(systems, APIdata, crop):
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

