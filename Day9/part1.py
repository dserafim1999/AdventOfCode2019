
def instructions(modes, instruction, i):
    parameters, j = [], 1
    global relative
    for mode in modes:
        if mode == 0: parameters.append(code[checkIndex(code, code[i+j])]) #j is the offset in the instruction, meaning for example that i+1 would be the parameter straight after the opcode
        elif mode == 1: parameters.append(code[checkIndex(code, i+j)])
        elif mode == 2: parameters.append(code[checkIndex(code, code[i+j]+relative)])
        j += 1

    if instruction == 1: 
        code[checkIndex(code, code[i+3])] = parameters[0] + parameters[1]
    elif instruction == 2: 
        code[checkIndex(code, code[i+3])] = parameters[0] * parameters[1]
    elif instruction == 3:
        value = int(input())
        if modes[0] == 0: code[checkIndex(code, code[i+1])] = value
        elif modes[0] == 1: code[checkIndex(code, i+1)] = value
        elif modes[0] == 2: code[checkIndex(code, code[i+1]+relative)] = value
    elif instruction == 4:
        print(parameters[0])
    elif instruction == 5:
        if parameters[0] != 0: return parameters[1]
        else: return i+3
    elif instruction == 6:
        if parameters[0] == 0: return parameters[1]
        else: return i+3
    elif instruction == 7:
        if parameters[0] < parameters[1]: code[checkIndex(code, code[i+3])] = 1
        else: code[checkIndex(code, code[i+3])] = 0
    elif instruction == 8: 
        if parameters[0] == parameters[1]: code[checkIndex(code, code[i+3])] = 1
        else: code[checkIndex(code, code[i+3])] = 0
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

i, relative = 0,0

while not code[i] == 99:
    modes = [int(i) for i in str(code[i]//100)]
    instruction =  code[i]%100
    while len(modes) != 2 and not instruction in (3,4,9):
        modes.insert(0,0)    
    modes.reverse()

    if instruction in (1,2,7,8):
        instructions(modes, instruction, i)
        i += 4   
    elif instruction in (3,4,9):
        instructions(modes, instruction, i)
        i += 2
    elif instruction == 5 or instruction == 6:
        i = instructions(modes, instruction, i)
    else:
        print("Something went wrong")
        exit()

