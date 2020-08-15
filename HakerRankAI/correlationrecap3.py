# https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem

P = [15,12,8,8,7,7,7,6,5,3]
H = [10,25,17,11,13,17,20,13,9,15]

avgX = sum(P)/len(P)
avgY = sum(H)/len(H)

slopeNumerator = sum([( (x - avgX) * (y - avgY) ) for (x,y) in zip(P,H)])
slopeDenominator = sum([(x - avgX)**2 for x in P])

slope = slopeNumerator/slopeDenominator
yIntercept = avgY - slope * avgX

score = yIntercept + slope * 10

print(round(score,1))
