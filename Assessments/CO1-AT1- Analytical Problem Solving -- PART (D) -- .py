from collections import deque

rows = 5
columns = 5

start = (1, 1)
goal = (5, 5)

blocked = {
    (2, 2),
    (2, 3),
    (3, 3),
    (4, 2),
    (4, 4)
}

moves = [
    (0, 1),    # Right
    (1, 0),    # Down
    (0, -1),   # Left
    (-1, 0)    # Up
]


def is_valid(cell):
    row, column = cell

    return (
        1 <= row <= rows
        and 1 <= column <= columns
        and cell not in blocked
    )


def get_neighbours(cell):
    row, column = cell
    neighbours = []

    for row_change, column_change in moves:
        next_cell = (
            row + row_change,
            column + column_change
        )

        if is_valid(next_cell):
            neighbours.append(next_cell)

    return neighbours


def make_path(parent, cell):
    path = []

    while cell is not None:
        path.append(cell)
        cell = parent[cell]

    path.reverse()
    return path


def breadth_first_search():
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            return make_path(parent, current)

        for next_cell in get_neighbours(current):
            if next_cell not in visited:
                visited.add(next_cell)
                parent[next_cell] = current
                queue.append(next_cell)

    return None


path = breadth_first_search()

print("BFS Path:")
print(path)

print("BFS Cost:")
print(len(path) - 1)
