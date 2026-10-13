from itertools import permutations

n = int(input("Enter number of cities: "))
cost = []

print("Enter the cost matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

cities = list(range(1, n))
min_cost = float('inf')
best_path = []

for path in permutations(cities):
    route = (0,) + path + (0,)
    total = 0

    for i in range(len(route) - 1):
        total += cost[route[i]][route[i + 1]]

    if total < min_cost:
        min_cost = total
        best_path = route

print("Minimum cost:", min_cost)
print("Best route:", " -> ".join(str(city + 1) for city in best_path))
