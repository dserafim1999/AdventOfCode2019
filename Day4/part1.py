file = open("input.txt","r")
r = [int(x) for x in file.read().split('-')]
consecutive, adjacent = False, False
passwords = 0

for i in range(r[0],r[1] + 1):
    i = str(i)
    for j in range(1,6):
        if i[j-1] == i[j]:
            consecutive = True
        if i[j-1] > i[j]:
            consecutive, adjacent = False, False
            break
        if j == 5 and i[j-1] <= i[j]:
            adjacent = True
    if consecutive and adjacent:
        passwords += 1 
    consecutive, adjacent = False, False
    

print(passwords)