def is_valid(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def map_coloring(regions, colors, neighbors, assignment):
    if len(assignment) == len(regions):
        return assignment

    region = next(r for r in regions if r not in assignment)

    for color in colors:
        if is_valid(region, color, assignment, neighbors):
            assignment[region] = color

            result = map_coloring(regions, colors, neighbors, assignment)

            if result:
                return result

            del assignment[region]

    return None


regions = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

solution = map_coloring(regions, colors, neighbors, {})

if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(region, ":", color)
else:
    print("No solution exists")
