import collections

file = open("input.txt","r")
r = [int(x) for x in file.read().split('-')]
passwords, count = [], 0

for i in range(r[0], r[1]+1):
    i = str(i)
    n, prev = 1, i[0]
    consecutive, adjacent = False, True

    for j in range(1,6):
        if i[j] == prev:
            consecutive = True
        if prev > i[j]:
            adjacent = False
            break
        prev = i[j]
    if consecutive and adjacent:
        passwords.append(i)

for p in passwords:
    if(2 in collections.Counter(p).values()):
        count += 1

print(count)