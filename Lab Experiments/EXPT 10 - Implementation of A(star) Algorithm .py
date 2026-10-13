def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_list.append((new_f, new_g, neighbor, path + [neighbor]))

    return None, -1


n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    node = input("Enter node name: ")
    graph[node] = []
    edges = int(input("Enter number of neighbors: "))

    for j in range(edges):
        neighbor, cost = input("Enter neighbor and cost: ").split()
        graph[node].append((neighbor, int(cost)))

heuristic = {}

for node in graph:
    heuristic[node] = int(input("Enter heuristic for " + node + ": "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, cost = astar(graph, heuristic, start, goal)

if path:
    print("Best path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found")
