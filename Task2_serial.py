from collections import defaultdict

def addEdge(x, y):
    graph[x].append(y)
    graph[y].append(x)

def addNeighbours(parent):
    visited[parent] = True
    neighbours = []
    for node in graph[parent]:
        if not visited[node]:
            visited[node] = True
            neighbours.append(node)
            distance[node] = distance[parent] + 1
    return neighbours

#def bfs(level):
    


v, e = map(int, input().split())


distance = [0] * v
graph = defaultdict(list)
visited = [False] * v

for _ in range(e):
    x, y = map(int, input().split())
    addEdge(x, y)

#bfs([0])

for i in range(len(distance)):
    print(f'Shortest distance from 0 to {i} = {distance[i]}')