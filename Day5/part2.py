def instructions(modes, instruction, i):
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
        if modes[0] == 0: code[code[i+1]] = int(input())
    elif instruction == 4:
        if modes[0] == 0: print(parameters[0])
        elif modes[0] == 1: print(parameters[0])
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

i = 0
while not code[i] == 99:
    modes = [int(i) for i in str(code[i]//100)]
    instruction =  code[i]%100
    while len(modes) != 2 and not instruction in (3,4):
        modes.insert(0,0)    
    modes.reverse()

    if instruction == 1 or instruction == 2:
        instructions(modes, instruction, i)
        i += 4   
    elif instruction == 3 or instruction == 4:
        instructions(modes, instruction, i)
        i += 2
    elif instruction == 5 or instruction == 6:
        i = instructions(modes, instruction, i)
    elif instruction == 7 or instruction == 8:
        instructions(modes, instruction, i)
        i += 4
    else:
        print("Something went wrong")
        exit()
    