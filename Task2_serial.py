from collections import defaultdict
graph = defaultdict(list)

def addEdge(x, y):
    graph[x].append(y)
    graph[y].append(x)

def bfs(source, dstance, v):
    visited = [False] * v

    q = []
    q.append(source)

    visited[source] = True

    while q:
        source = q.pop(0)

        for vertex in graph[source]:
            if not visited[vertex]:
                q.append(vertex)
                distance[vertex] = distance[source] + 1

                visited[vertex] = True


v, e = map(int, input().split())
distance = [0] * v

for _ in range(e):
    x, y = map(int, input().split())
    addEdge(x, y)

bfs(0, distance, v)

for i in range(len(distance)):
    print(f'Shortest distance from 0 to {i} = {distance[i]}')