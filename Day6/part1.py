def find_shortest_path(graph, start, end, path=[]):
    """
    __source__='https://www.python.org/doc/essays/graphs/'
    __author__='Guido van Rossum'
    """
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

#----------------------------------------------------#
#REALLY SLOW FOR BIG INPUTS
#----------------------------------------------------#

with open("input.txt") as file:
    orbits = file.read().split('\n')

graph, planets = {}, set()

for orbit in orbits:
    node, child = orbit.split(')')
    planets.add(child) #guarantes every planet is inserted since every planet revolves around another
    if node in graph:
        graph[node].append(child)
    else:
        graph[node] = [child]

norbits = 0
for planet in planets:
    norbits += len(find_shortest_path(graph, 'COM', planet,[])) - 1 

print(norbits)

