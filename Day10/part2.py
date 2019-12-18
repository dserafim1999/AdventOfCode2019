from math import acos, sqrt, pi
import operator

def angleBetweenVectors (v1, v2, sign):
    '''
    deduction from cross product formula
    '''
    if v1 == v2: return 0
    return sign * acos((v1[0]*v2[0]+v1[1]*v2[1])/round(sqrt(v1[0]**2+v1[1]**2)*sqrt(v2[0]**2+v2[1]**2),13))

def angleBetweenAsteroids (asteroid1, asteroid2, yaxis):
    '''
    calculates angle between vector that goes from the current asteroid to the center and other that goes from current asteroid to another
    '''
    vector1 = (yaxis[0] - asteroid1[0], yaxis[1] - asteroid1[1])
    vector2 = (asteroid2[0] - asteroid1[0], asteroid2[1] - asteroid1[1])
    if asteroid2[1] >= asteroid1[1]: sign = -1
    else: sign = 1
    return angleBetweenVectors(vector1, vector2, sign)

def euclideanDistance (pt1, pt2):
    return sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
#---------------------------------------------------------------------#

with open("input.txt") as file:
    text = file.read().split('\n')

asteroidBelt = [[j for j in i] for i in text]
asteroidPos = []
asteroidAngles = []

for i in range(len(asteroidBelt)):
    for j in range(len(asteroidBelt[i])):
        if asteroidBelt[i][j] == '#': asteroidPos.append((i,j))

asteroidDetected = [0 for i in range(len(asteroidPos))]

for i in range(len(asteroidPos)):
    current = asteroidPos[i]
    yaxis = (current[0] - len(asteroidBelt[0]), current[1]) #creates a point outside of the asteroid belt to create a vector thats paralel to the x axis in order to calculate angles
    asteroidAngles.append([])
    for j in range(len(asteroidPos)):
        if asteroidPos[i] == asteroidPos[j]: 
            asteroidAngles[i].append('x')
            continue
        angle = -round(angleBetweenAsteroids(current, asteroidPos[j], yaxis), 6)
        if angle < 0: angle = round(pi + pi + angle,6) 
        asteroidAngles[i].append(angle)
    asteroidAngles[i].remove('x') #removes current asteroid from count since an asteroid can't detect itself
    asteroidDetected[i] = len(set(asteroidAngles[i]))
    
station = asteroidPos[asteroidDetected.index(max(asteroidDetected))]
asteroidPos.remove(station)
angles = [[asteroidAngles[asteroidDetected.index(max(asteroidDetected))][i] , round(euclideanDistance(station, asteroidPos[i]), 6) , asteroidPos[i]] for i in range(len(asteroidPos))]
angles.sort()

n_vaporized = 0
previous = -1
j = 0

#algorithm to calculate the angle based on blocked asteroids
for i in range(len(angles)):
    if angles[i][0] == previous:
        previous = angles[i][0]
        j += 1
        angles[i][0] = round(angles[i][0] + pi * 2 * j, 6) #adds n full circles to angle depending on how many asteroids are blocking it
    else: 
        j = 0
        previous = angles[i][0]
angles.sort()

print(angles[199][2][1]*100 + angles[199][2][0])