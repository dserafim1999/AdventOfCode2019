import math

width = 25
height = 6

with open("input.txt") as file:
    text = file.read()

layers = []
colors = ['2' for i in range(width*height)]
x,j = 0,0
while x != len(text):
    layerPixels = text[x:x+width*height]
    for i in range(len(layerPixels)):
        if colors[i] != '2':
            continue
        colors[i] = layerPixels[i]
    x += width*height

row = ''
for i in range(len(colors)):
    if colors[i] == '0': char = ' '
    elif colors[i] == '1': char = '█'
    row += char
    j += 1
    if j == width:
        print(row)
        row = ''
        j = 0
      
 

