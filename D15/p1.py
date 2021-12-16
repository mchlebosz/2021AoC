from pathlib import Path
from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)]
                      for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight1, weight2):
        self.edges[u][v] = weight1
        self.edges[v][u] = weight2


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


script_location = Path(__file__).absolute().parent
with open(script_location / 'input.txt', mode='r', encoding='utf-8') as f:
    inpu = list(
        map(lambda x: list(map(int, x[:len(x)-1])), f.readlines()))

print(inpu)

graphSizeY = len(inpu)
graphSizeX = len(inpu[0])

print(graphSizeY, graphSizeX)

g = Graph(graphSizeY*graphSizeX)

for i in range(graphSizeY):
    for j in range(graphSizeX):
        index = j + (i * graphSizeX)
        if i+1 < graphSizeY:
            g.add_edge(index, index + graphSizeX, inpu[i+1][j], inpu[i][j])
        if j+1 < graphSizeX:
            g.add_edge(index, index + 1, inpu[i][j + 1], inpu[i][j])


# print(g)
D = dijkstra(g, 0)
print(D)

result = [[" ".join([str(D[j + (i * graphSizeX)])
                     for j in range(graphSizeX)])]for i in range(graphSizeY)]


print("Distance from vertex 0 to vertex", graphSizeX *
      graphSizeY-1, "is", D[graphSizeX*graphSizeY-1])


with open(script_location / "output.out", mode='w', encoding='utf-8') as f:
    for i in result:

        f.write(" ".join(i)+"\n")
