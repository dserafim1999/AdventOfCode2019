def calculateFuel(fuel):
    result = 0
    while fuel > 0:
        fuel = int(fuel/3) - 2
        if fuel <= 0:
            return result
        result += fuel
    return result

file = open("input1.txt","r")

modules = file.readlines()
result = 0

for module in modules:
    fuel = calculateFuel(int(module))
    result += fuel

print(result)