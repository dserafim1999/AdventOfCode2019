def intcodeProgram(code):
    i = 0
    while  not code[i] == 99:
        if code[i] == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
            i += 4   
        elif code[i] == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
            i += 4   
        elif code[i] == 99:
            exit()
        else:
            print("Something went wrong")
            exit()
    return code[0]
#---------------------------------------------------#

with open("input.txt") as file:
    text = file.read()

code = [int(x) for x in text.split(',')]

for noun in range(0,100):
    for verb in range(0,100):
        auxCode = code.copy()
        auxCode[1], auxCode[2] = noun, verb
        if intcodeProgram(auxCode) == 19690720:
            print(100*noun+verb)
            exit()