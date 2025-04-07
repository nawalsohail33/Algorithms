graph= {
    'A':['F','D','B','E'],
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
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for i in graph[root]:
            dfs(visited,graph,i)
dfs(visited,graph,'A')
