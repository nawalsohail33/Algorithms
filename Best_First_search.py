import heapq

#sb sy pehly graph define kryn gy
graph ={
    1: [(2,15),(3,4)],
    2:[(4,3),(6,7),(7,10)],
    3:[(4,2),(5,6)],
    4:[(5,4)],
    5:[(6,4)],
    6:[(7,5)],
    7:[]
}
#heuristic values define kryn
heuristic = {
    1:16,
    2:11,
    3:10,
    4:7,
    5:9,
    6:4,
    7:0
}
#greedy wala function
def greedy_best(graph,heuristic,start,target):
    visited=set()
    priority_queue=[(heuristic[start],start)]
    while priority_queue:
        h_value,current_node=heapq.heappop(priority_queue)
        if current_node not in visited:
            visited.add(current_node)
            print("Visited ",visited)
        if current_node==target:
            print("Target reached ",current_node)
            print("Traversal path ",visited)
            return
        for neighbour,cost in graph[current_node]:
            if neighbour not in visited:
                heapq.heappush(priority_queue,(heuristic[neighbour],neighbour))
    print('Target not found')
    
greedy_best(graph,heuristic,1,7)
