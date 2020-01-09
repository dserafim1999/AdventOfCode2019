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

#---------------------------------------------------#

with open("input.txt") as file:
    text = file.read()

code = [int(x) for x in text.split(',')]
index, relative  =  0,0
tiles = {}

while code[index] != 99:
    x, index = runIntcodeComputer(index, auto = True)
    y, index = runIntcodeComputer(index, auto = True)
    tileid, index = runIntcodeComputer(index, auto = True)
    if code[index] == 99: continue
    tiles[(x,y)] = tileid

ntilesid = [(k, len(list(v))) for k, v in itertools.groupby(sorted(tiles.values()))] #counts occurences of same values in dictionary (tile type, n of tiles)
print('Number of type 2 tiles:', ntilesid[2][1])
