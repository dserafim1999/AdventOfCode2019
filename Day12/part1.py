with open("input.txt") as file:
    text = file.read().split('\n')

positions, tempPositions = [],[] 
velocities = [] 
energy = []

for x in text:
    position = []
    for i in range(3): 
        position.append(int(x[x.find('=')+1 : x.find(',')]))
        x = x[x.find(',')+1:]
    positions.append(position)
    velocities.append([0,0,0])

for step in range(1000):
    tempPositions = [[0,0,0] for i in range(len(positions))]
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i == j: continue
            for k in range(len(positions[i])):
                if positions[i][k] > positions[j][k]: 
                    velocities[i][k] -= 1
                elif positions[i][k] < positions[j][k]: 
                    velocities[i][k] += 1
        for k in range(len(positions[0])): #random positions since positions have the same size
            tempPositions[i][k] = positions[i][k] + velocities[i][k]
    
    for i in range(len(positions)): 
        positions[i] = tempPositions[i]

energy = 0
for i in range(len(positions)):
    pot, kin = sum(abs(k) for k in positions[i]), sum(abs(k) for k in velocities[i])
    energy += pot * kin

print(energy)

    
    
