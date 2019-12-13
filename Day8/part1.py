import math

width = 25
height = 6

with open("input.txt") as file:
    text = file.read()

layers, digitcount = [],[]
x,i = 0,0
while x!= len(text):
    layer = []
    digitcount.append([0,0,0])
    for j in range(height):
        layer.append(text[x:x+width])
        for k in layer[j]:
            if k == '0': digitcount[i][0] += 1
            elif k == '1': digitcount[i][1] += 1
            elif k == '2': digitcount[i][2] += 1
        x += width
    i += 1
    layers.append(layer)

min_0, min_i = math.inf, 0
for i in range(len(digitcount)):
    if int(digitcount[i][0]) < min_0:
        min_0 = int(digitcount[i][0])
        min_i = i

print(digitcount[min_i][1]*digitcount[min_i][2])