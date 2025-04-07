import heapq

# Define the graph as an adjacency list
graph = {
    'A': [('B', 9), ('E', 8)],
    'B': [('C', 60),('G',11)],
    'C': [('D', 20)],
    'D': [('H', 40)],
    'E': [('F',10)],
    'F': [('G',13)],
    'G': [('H',14)],
    'H':[]
}

def uniform_cost_search(start_node,goal_node):
    priority_queue=[(0,start_node)]
    min_cost={start_node:0}
    print("Initialization")
    print("Priority Queue",priority_queue)
    print("Minimum Cost",min_cost)
    while priority_queue:
        current_cost,current_node=heapq.heappop(priority_queue)
        print("Exploring node",current_node,"with cost of",current_cost)
        if current_node==goal_node:
            print("Goal reached",current_node,"and the cost is",current_cost)
            return
        for i,cost in graph[current_node]:
            new_cost=current_cost+cost
            print("Neighbor",i,"Cost",cost)
            if i not in min_cost or new_cost<min_cost[i]:
                min_cost[i]=new_cost
                heapq.heappush(priority_queue,(new_cost,i))
                print("Updated Cost",new_cost)
                print("Priority Queue",priority_queue)
    print("goal unreachable")


start_node = 'A'
goal_node = 'H'
uniform_cost_search(start_node, goal_node)
