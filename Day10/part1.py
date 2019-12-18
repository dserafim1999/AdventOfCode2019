from math import acos, sqrt

def angleBetweenVectors (v1, v2, sign):
    '''
    deduction from cross product formula
    '''
    if v1 == v2: return 0
    return sign * acos((v1[0]*v2[0]+v1[1]*v2[1])/round(sqrt(v1[0]**2+v1[1]**2)*sqrt(v2[0]**2+v2[1]**2),13))

def angleBetweenAsteroids (asteroid1, asteroid2, xaxis):
    '''
    calculates angle between vector that goes from the current asteroid to the center and other that goes from current asteroid to another
    '''
    vector1 = (xaxis[0] - asteroid1[0], xaxis[1] - asteroid1[1])
    vector2 = (asteroid2[0] - asteroid1[0], asteroid2[1] - asteroid1[1])
    if asteroid2[0] > asteroid1[0]: sign = 1
    else: sign = -1
    return angleBetweenVectors(vector1, vector2, sign)

with open("input.txt") as file:
    text = file.read().split('\n')

asteroidBelt = [[j for j in i] for i in text]
asteroidPos = []

for i in range(len(asteroidBelt)):
    for j in range(len(asteroidBelt[i])):
        if asteroidBelt[i][j] == '#': asteroidPos.append((i,j))

asteroidDetected = [0 for i in range(len(asteroidPos))]

for i in range(len(asteroidPos)):
    current = asteroidPos[i]
    xaxis = (current[0], current[1] + len(asteroidBelt[0])) #creates a point outside of the asteroid belt to create a vector thats paralel to the x axis in order to calculate angles
    asteroidAngles = []
    #print('-----',asteroidPos[i],'-----')
    for j in range(len(asteroidPos)):
        if asteroidPos[i] == asteroidPos[j]: 
            asteroidAngles.append(-1)
            #print(asteroidPos[j], '---> ', asteroidAngles[j])
            continue
        asteroidAngles.append(round(angleBetweenAsteroids(current, asteroidPos[j], xaxis), 6))
        #print(asteroidPos[j], '---> ', asteroidAngles[j])
    #print(set(asteroidAngles), 'len: ',len(set(asteroidAngles))-1)
    asteroidDetected[i] = len(set(asteroidAngles))-1 #removes current asteroid from count since an asteroid can't detect itself
    #asteroidDetected[i] = (asteroidPos[i],len(set(asteroidAngles))-1) #removes current asteroid from count since an asteroid can't detect itself

    
print(max(asteroidDetected))