import itertools

def runIntcodeComputer(input,phase = -1,value = -1,auto = False):
    i = 0
    j = 1
    while not input[i] == 99:
        modes = [int(i) for i in str(input[i]//100)]
        instruction =  input[i]%100
        if auto:
            if instruction == 3:
                if j == 1:
                    inputAuto = phase
                    i = runInstruction(modes, instruction, i, auto, inputAuto)
                    j +=1
                    continue
                else: 
                    inputAuto = value
                    i = runInstruction(modes, instruction, i, auto, inputAuto)
                    continue
            elif instruction == 4:
                    output = runInstruction(modes, instruction, i, auto)
                    return output
        while len(modes) != 2 and not instruction in (3,4):
            modes.insert(0,0)    
        modes.reverse()
        i = runInstruction(modes, instruction, i)

def runInstruction(modes, instruction, i, auto = False, value = -1):
    if instruction == 1 or instruction == 2:
        processInstruction(modes, instruction, i)
        return i + 4   
    elif instruction == 3 or instruction == 4:
        if auto and instruction == 4: return processInstruction(modes, instruction, i, auto, value)
        else: processInstruction(modes, instruction, i, auto, value)
        return i + 2
    elif instruction == 5 or instruction == 6:
        return processInstruction(modes, instruction, i)
    elif instruction == 7 or instruction == 8:
        processInstruction(modes, instruction, i)
        return i + 4
    else:
        print("Something went wrong")
        exit()

def processInstruction(modes, instruction, i, auto = False, value = -1):
    parameters, j = [], 1
    for mode in modes:
        if mode == 0: parameters.append(code[code[i+j]]) #j is the offset in the instruction, meaning for example that i+1 would be the parameter straight after the opcode
        elif mode == 1: parameters.append(code[i+j])
        j += 1

    if instruction == 1: 
        code[code[i+3]] = parameters[0] + parameters[1]
    elif instruction == 2: 
        code[code[i+3]] = parameters[0] * parameters[1]
    elif instruction == 3: 
        if modes[0] == 0: 
            if not auto: code[code[i+1]] = int(input())
            else: code[code[i+1]] = value
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
        if parameters[0] < parameters[1]: code[code[i+3]] = 1
        else: code[code[i+3]] = 0
    elif instruction == 8: 
        if parameters[0] == parameters[1]: code[code[i+3]] = 1
        else: code[code[i+3]] = 0

#---------------------------------------------------#

with open("input.txt") as file:
    text = file.read()

code = [int(x) for x in text.split(',')]
signals = []

for permutation in list(itertools.permutations([0,1,2,3,4])):
    output = 0
    for phase in permutation:
        output = runIntcodeComputer(code, phase, output, True)
    signals.append(output)
    
print(max(signals))