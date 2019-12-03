with open("input1.txt") as file:
    text = file.read()

code = [ int(x) for x in text.split(',')]
code[1], code[2], i = 12,2,0

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
print(code[0])