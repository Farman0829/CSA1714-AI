from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = {start}

    moves = [
        (1, 0), (2, 0), (0, 1),
        (0, 2), (1, 1)
    ]

    while queue:
        state, path = queue.popleft()
        m, c, b = state

        if state == goal:
            print("Solution:")
            for step in path:
                print(step)
            return

        for dm, dc in moves:
            if b == 0:
                new_state = (m - dm, c - dc, 1)
                action = f"Move {dm} Missionary(s) and {dc} Cannibal(s) from Left to Right"
            else:
                new_state = (m + dm, c + dc, 0)
                action = f"Move {dm} Missionary(s) and {dc} Cannibal(s) from Right to Left"

            if is_valid(new_state[0], new_state[1]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [action]))

solve()
