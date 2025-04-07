#BFS code for whole traversal
import collections
def bfs(graph,node):
    visited=set()
    queue=collections.deque([node])
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                queue.append(i)
    print(visited)
    
graph = {0: [1, 2, 3], 1: [0, 2], 2: [1, 0, 4], 3: [0], 4: [2]}
bfs(graph,0)
