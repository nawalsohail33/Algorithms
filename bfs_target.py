import collections
def bfs(graph,start,target):
    visited=set()
    queue=collections.deque([start])
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print("Visited ",visited)
        if vertex==target:
            print("Target reached ",vertex)
            print("Traversal path ",visited)
            return
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print("Not found")
    
graph = {0:[1,2,3],1:[0,2],2:[1,0,4],3:[0],4:[2]}
bfs(graph,0,3)
