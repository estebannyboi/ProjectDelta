#Eliminates systems that produce extreme temperatures

take crop as input and find growth temp range

run thermal model at 12 points throughout the day on each system

for each unit area, if temp is in range, give it score of 1, if outside, give it 0

add sum of scores at any point in the day with the rest to produce final score

Highest score (including tied) gets sent to DLIScore function