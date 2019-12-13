import itertools

def runIntcodeComputer(amp, i, phase = -1, value = -1, auto = False):
    j = 1
    while not code[amp][i] == 99:
        modes = [int(i) for i in str(code[amp][i]//100)]
        instruction = code[amp][i]%100
        if auto:
            if instruction == 3:
                if j == 1:
                    inputAuto = phase
                    i = runInstruction(amp, modes, instruction, i, auto, inputAuto)
                    j +=1
                    continue
                else: 
                    inputAuto = value
                    i = runInstruction(amp, modes, instruction, i, auto, inputAuto)
                    continue
            elif instruction == 4:
                    output, i = runInstruction(amp, modes, instruction, i, auto)
                    return (output, i)
                    
        while len(modes) != 2 and not instruction in (3,4):
            modes.insert(0,0)    
        modes.reverse()
        i = runInstruction(amp, modes, instruction, i)
    return (value, i)
    

def runInstruction(amp, modes, instruction, i, auto = False, value = -1):
    if instruction == 1 or instruction == 2:
        processInstruction(amp, modes, instruction, i)
        return i + 4   
    elif instruction == 3 or instruction == 4:
        if auto and instruction == 4: return (processInstruction(amp, modes, instruction, i, auto, value), i + 2)
        else: processInstruction(amp, modes, instruction, i, auto, value)
        return i + 2
    elif instruction == 5 or instruction == 6:
        return processInstruction(amp, modes, instruction, i)
    elif instruction == 7 or instruction == 8:
        processInstruction(amp, modes, instruction, i)
        return i + 4
    else:
        print("Something went wrong")
        exit()

def processInstruction(amp,modes, instruction, i, auto = False, value = -1):
    parameters, j = [], 1
    for mode in modes:
        if mode == 0: parameters.append(code[amp][code[amp][i+j]]) #j is the offset in the instruction, meaning for example that i+1 would be the parameter straight after the opcode
        elif mode == 1: parameters.append(code[amp][i+j])
        j += 1

    if instruction == 1: 
        code[amp][code[amp][i+3]] = parameters[0] + parameters[1]
    elif instruction == 2: 
        code[amp][code[amp][i+3]] = parameters[0] * parameters[1]
    elif instruction == 3: 
        if modes[0] == 0: 
            if not auto: code[amp][code[amp][i+1]] = int(input())
            else: code[amp][code[amp][i+1]] = value
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
        if parameters[0] < parameters[1]: code[amp][code[amp][i+3]] = 1
        else: code[amp][code[amp][i+3]] = 0
    elif instruction == 8: 
        if parameters[0] == parameters[1]: code[amp][code[amp][i+3]] = 1
        else: code[amp][code[amp][i+3]] = 0

#---------------------------------------------------#

with open("input.txt") as file:
    text = file.read()

code = [[int(x) for x in text.split(',')] for j in range(5)]
signals = []

#for phases in list(itertools.permutations([5,6,7,8,9])):
i = 0
phases = [9,8,7,6,5]
output = 0
indices = [0,0,0,0,0]
while code[4][indices[4]] != 99:
    output, indices[i] = runIntcodeComputer(i, indices[i], phases[i], output, True)
    i = (i+1)%5
signals.append(output)

print(signals)