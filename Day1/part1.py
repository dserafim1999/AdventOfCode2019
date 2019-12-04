file = open("input.txt","r")

modules = file.readlines()
result = 0

for module in modules:
    fuel = int(int(module)/3) - 2
    result += fuel

print(result)