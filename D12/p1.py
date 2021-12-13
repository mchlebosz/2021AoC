from igraph import *
from pathlib import Path
script_location = Path(__file__).absolute().parent
with open(script_location / 'test.txt', mode='r', encoding='utf-8') as f:
    inpu = list(map(lambda x: list(x[:len(x)-1].split("-")), f.readlines()))

connections = dict()
vertices = set()

for item in inpu:
    vertices.add(item[0])
    vertices.add(item[1])

    if not item[0] in connections:
        connections[item[0]] = set()
    connections[item[0]].add(item[1])
    if not item[1] in connections:
        connections[item[1]] = set()
    connections[item[1]].add(item[0])

vertDict = dict()
i = 0
for item in connections:
    vertDict[item] = i
    i += 1

print(connections)
print(len(sorted(vertices)))

g = Graph()
g.add_vertices(len(sorted(vertices)))
for item in inpu:
    g.add_edges([(vertDict[item[0]], vertDict[item[1]])])

print(g)
print(vertDict)
result = list()
result.append(4)
result = inpu


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
