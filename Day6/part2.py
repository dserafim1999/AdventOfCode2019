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

def distance_between_nodes(graph, pt1, pt2):
    path1,path2 = find_shortest_path(graph, 'COM', pt1, []),find_shortest_path(graph, 'COM', pt2, [])
    path = []

    for node in path1:
        if not node in path2:
            path.append(node)
    for node in path2:
        if not node in path1 and not node in path:
            path.append(node)
    
    return len(path)


#----------------------------------------------------#

with open("input.txt") as file:
    orbits = file.read().split('\n')

graph, planets = {}, set()

for orbit in orbits:
    node, child = orbit.split(')')
    if child == 'YOU':
        you_orbit = node
    elif child == 'SAN':
        san_orbit = node
    planets.add(child) #guarantes every planet is inserted since every planet revolves around another
    if node in graph:
        graph[node].append(child)
    else:
        graph[node] = [child]

print(distance_between_nodes(graph, you_orbit, san_orbit))


