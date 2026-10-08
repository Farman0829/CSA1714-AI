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
    (0, 1),    
    (1, 0),    
    (0, -1),   
    (-1, 0)    
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


def depth_first_search():
    stack = [start]
    visited = {start}
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            return make_path(parent, current)

        neighbours = get_neighbours(current)

        for next_cell in reversed(neighbours):
            if next_cell not in visited:
                visited.add(next_cell)
                parent[next_cell] = current
                stack.append(next_cell)

    return None


path = depth_first_search()

print("DFS Path:")
print(path)

print("DFS Cost:")
print(len(path) - 1)
