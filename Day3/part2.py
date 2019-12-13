#using negative numbers for positions to simplify central point position (0,0) and manhattan distance to it

def calculateIntersections(positions):
    seen = set()
    intersection = []
    for x in positions:
        if x not in seen:
            seen.add(x)
        else:
            intersection.append(x)
    return list(filter(lambda a: a != (0,0), intersection)) #removes all instances of (0,0)

def removeIntersections(positions):
    seen = set()
    unique = []
    for x in positions:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    return unique

def calculateManhattanDistance(pt1, pt2):
    return abs(pt2[0]-pt1[0]) + abs(pt2[1]-pt1[1])

#-------------------------------------------------------------------------------------------#

with open("input.txt") as file:
    text = file.read()

instr = text.split('\n')
instr = [instr[i].split(',') for i in range(len(instr))]
totalPositions = []  #positions occupied by all wires
positions = []

for i in range(len(instr)):
    tempPositions = [(0,0)]
    positions.append([])
    for x in instr[i]: #adds position directly to the (right/left/up/down) of the last position added to the positions array
        if(x[0] == 'R'):
            for j in range(int(x[1:])):
                tempPositions.append([tempPositions[-1][0] + 1, tempPositions[-1][1]]) 
        elif(x[0] == 'L'):
            for j in range(int(x[1:])):
                tempPositions.append([tempPositions[-1][0] - 1, tempPositions[-1][1]])
        elif(x[0] == 'U'):
            for j in range(int(x[1:])):
                tempPositions.append([tempPositions[-1][0], tempPositions[-1][1] + 1])
        elif(x[0] == 'D'):
            for j in range(int(x[1:])):
                tempPositions.append([tempPositions[-1][0], tempPositions[-1][1] - 1])
    tempPositions = [tuple(x) for x in tempPositions]
    positions[i] = tempPositions
    totalPositions += removeIntersections(tempPositions) #adds wire positions without intersections with itself to list of all wire positions
        


intersections = calculateIntersections(totalPositions) 

distances = []


for x in intersections:
    calculating1, calculating2, i = True, True, 0
    while calculating1 or calculating2:
        if calculating1:
            if positions[0][i] == x:
                distance1 = i
                calculating1 = False
        if calculating2:
            if positions[1][i] == x:
                distance2 = i
                calculating2 = False
        i += 1
    distances.append(distance1+distance2)
        
print(min(distances))





        
        

