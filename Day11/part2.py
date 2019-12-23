import itertools

def runIntcodeComputer(i, value = -1, auto = False):
    while not code[i] == 99:
        modes = [int(i) for i in str(code[i]//100)]
        instruction = code[i]%100
        if auto:
            if instruction == 3:
                i = runInstruction(modes, instruction, i, auto, value)
                continue
            elif instruction == 4:
                    output, i = runInstruction(modes, instruction, i, auto)
                    return (output, i)
        while len(modes) < 3 and not instruction in (3,4):
            modes.insert(0,0)    
        modes.reverse()
        i = runInstruction(modes, instruction, i)
    return (value, i)
    

def runInstruction(modes, instruction, i, auto = False, value = -1):
    if instruction in (1,2,7,8):
        processInstruction(modes, instruction, i)
        return i + 4   
    elif instruction in (3,4,9):
        if auto and instruction == 4: return (processInstruction(modes, instruction, i, auto, value), i + 2)
        else: processInstruction(modes, instruction, i, auto, value)
        return i + 2
    elif instruction == 5 or instruction == 6:
        return processInstruction(modes, instruction, i)
    else:
        print("Something went wrong")
        exit()

def processInstruction(modes, instruction, i, auto = False, value = -1):
    parameters, j = [], 1
    global relative
    for mode in modes: #j is the offset in the instruction, meaning for example that i+1 would be the parameter straight after the opcode
        if mode == 0: 
            if j < 3: parameters.append(code[checkIndex(code, code[i+j])])
            elif j == 3: parameters.append(code[i+j])
        elif mode == 1: parameters.append(code[i+j])
        elif mode == 2: 
            if j < 3: parameters.append(code[checkIndex(code, code[i+j] + relative)])
            elif j == 3: parameters.append(code[i+j] + relative)
        j += 1

    if instruction == 1: 
        code[checkIndex(code, parameters[2])] = parameters[0] + parameters[1]
    elif instruction == 2: 
        code[checkIndex(code, parameters[2])] = parameters[0] * parameters[1]
    elif instruction == 3:
        if not auto: value = int(input())
        if modes[0] in (0,1): code[checkIndex(code, code[i+1])] = value
        elif modes[0] == 2: code[checkIndex(code,code[i+1]+relative)] = value
    elif instruction == 4:
        if not auto: print(parameters[0])
        else: return parameters[0]
    elif instruction == 5:
        if parameters[0] != 0: return parameters[1]
        else: return i+3
    elif instruction == 6:
        if parameters[0] == 0: return parameters[1]
        else: return i+3
    elif instruction == 7:
        if parameters[0] < parameters[1]: code[checkIndex(code, parameters[2])] = 1
        else: code[checkIndex(code, parameters[2])] = 0
    elif instruction == 8: 
        if parameters[0] == parameters[1]: code[checkIndex(code, parameters[2])] = 1
        else: code[checkIndex(code, parameters[2])] = 0
    elif instruction == 9:
        relative += parameters[0]

def checkIndex(code, i):
    j = len(code)
    if i >= j:
        while j <= i:
            code.append(0)
            j += 1
    return i

def calculateNextPosition(position, direction):
    global rotation
    if direction == 0:
        if rotation == 0: rotation = 3
        else: rotation -= 1
    elif direction == 1: rotation = (rotation+1)%4

    if rotation == 0: return (position[0], position[1] + 1)
    elif rotation == 1: return (position[0] + 1, position[1])
    elif rotation == 2: return (position[0], position[1] - 1)
    elif rotation == 3: return (position[0] - 1, position[1])

#---------------------------------------------------#

with open("input.txt") as file:
    text = file.read()

code = [int(x) for x in text.split(',')]
index, relative, color = 0, 0, 1
rotation = 1 #0 = up, 1 = right, 2 = down, 3 = left
currentPos = (0,0)
panelColors = {(0,0): color}

while code[index] != 99:
    if currentPos not in panelColors:
        panelColors[currentPos] = 0
    color, index = runIntcodeComputer(index, panelColors[currentPos], True)
    direction, index = runIntcodeComputer(index, panelColors[currentPos], True) 
    panelColors[currentPos] = color
    currentPos = calculateNextPosition(currentPos, direction)

coordinates = list(panelColors.keys())
x_s, y_s = [x[0] for x in coordinates], [x[1] for x in coordinates]

if abs(min(x_s)) > abs(min(y_s)): offset = abs(min(x_s))
else: offset = abs(min(y_s))

x_s, y_s = [x + offset for x in x_s], [y + offset for y in y_s]
panels = [(x,y) for x,y in zip(x_s, y_s)]

ship = [[' ' for y in range(max(y_s) + 1)] for x in range(max(x_s) + 1)]

for panel in panels:
    if panelColors[(panel[0] - offset, panel[1] - offset)] == 1: ship[panel[0]][panel[1]] = '█'

ship.reverse()
for i in range(max(x_s) - min(x_s) + 1):
    ship[i].reverse()
    print("".join(ship[i]))
