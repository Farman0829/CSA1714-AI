import heapq

def manhattan(state):
    distance = 0
    for i in range(16):
        if state[i] != 0:
            goal = state[i] - 1
            distance += abs(i // 4 - goal // 4) + abs(i % 4 - goal % 4)
    return distance

def solve(start):
    goal = tuple(list(range(1, 16)) + [0])
    pq = [(manhattan(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)
        zero = state.index(0)
        row, col = zero // 4, zero % 4

        moves = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1)
        ]

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 4 and 0 <= nc < 4:
                new_pos = nr * 4 + nc
                new_state = list(state)
                new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
                new_state = tuple(new_state)

                if new_state not in visited:
                    heapq.heappush(
                        pq,
                        (g + 1 + manhattan(new_state),
                         g + 1, new_state, path + [state])
                    )

    return None

start = tuple(map(int, input("Enter 16 puzzle numbers (0 for blank): ").split()))

solution = solve(start)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        for i in range(0, 16, 4):
            print(*state[i:i+4])
        print()
else:
    print("No solution found.")
