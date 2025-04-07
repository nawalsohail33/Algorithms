graph= {
    'A':['B','F','D','E'],
    'B':['K','J'],
    'K':['N','M'],
    'D':['G'],
    'E':['C','H','I'],
    'I':['L'],
    'N':[],
    'M':[],
    'G':[],
    'F':[],
    'J':[],
    'C':[],
    'H':[],
    'L':[]
}
visited=set()
path=[]
def dfs(visited,graph,start,target):
    if start not in visited:
        visited.add(start)
        path.append(start)
    if start==target:
        print("Goal reached ",start)
        print("traversal path ",path)
        return True
    for i in graph[start]:
        if dfs(visited,graph,i,target):
            return True
    return False

dfs(visited,graph,'A','G')
