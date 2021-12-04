import multiprocessing as mp
from collections import defaultdict

graph = defaultdict(list)
visited = []

distance = []

def addNeighbours(parent):
    visited[parent] = True
    neighbours = []
    for node in graph[parent]:
        if not visited[node]:
            neighbours.append(node)
            visited[node] = True
            distance[node] = distance[parent] + 1
    return neighbours    

def addEdge(u, v):    
    graph[u].append(v)   
    graph[v].append(u)
    
def parallelBFS(level):
    while(level) :    
        newLevel = []
        cpu_count = mp.cpu_count()
        pool = mp.Pool(processes = cpu_count)
        newLevel = pool.map(addNeighbours, [node for node in level])
        flatNewLevel = []
        for lst in newLevel:
            for node in lst:
                flatNewLevel.append(node)   
        level = flatNewLevel


if __name__ == '__main__':
    v, e = map(int, input().split())    #v = number of edges, e = number of edges
    
    visited = mp.Array('i', v)
    distance = mp.Array('i', v)

    for _ in range(e):
        x, y  = map(int, input().split())
        addEdge(x, y)

    parallelBFS([0])
    
    for i in range(len(distance)):
        print(f'Shortest distance between 0 and {i} = {distance[i]}')