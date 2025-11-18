import math

found = False

# Reading Map
with open('map.txt', 'r') as f:
    raw_map = f.readline().strip().split()
    size_x = int(raw_map[0])
    size_y = int(raw_map[1])

    map_grid = []
    # for line in raw_map: #unlike c, python reads files line by line
    #     row = line.strip().split()
    #     map_grid.append(row)
    for line in f:
        row = list(line.strip().split())  # Using list() is robust for map grids
        map_grid.append(row)

# Start Point and Goal Point
for x, row in enumerate(map_grid):
    for y, value in enumerate(row):
        if value == 'S':
            start = (x, y)
        if value == 'G':
            goal = (x, y)

# Setting Start Point as Current Point
current = [start[0],start[1]]

# Defining Neighbors
directions = [(-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1)]

neighbors = []
for dx, dy in directions:
    neighbor = (current[0] + dx, current[1] + dy)
    neighbors.append(neighbor)

# Printing Function
def print_map(map_grid):
    print()
    for row in map_grid:
        print(" ".join(str(cell) for cell in row))
# Main

while found == False:
    print_map(map_grid)

    ## highlighting neighboring nodes
    for x, y in neighbors:
        if 0 <= x < size_x and 0 <= y < size_y:
            if map_grid[x][y] == '.':
                map_grid[x][y] = 'o'
    print_map(map_grid)

    ## finding the A* value of each neighboring node
    least_val = size_x*size_y
    for x, y in neighbors:
        if 0 <= x < size_x and 0 <= y < size_y:
            if map_grid[x][y] == 'G':
                found = True
                break
            if map_grid[x][y] == 'o':
                current_distance = math.sqrt((x - current[0]) ** 2 + (y - current[1]) ** 2)
                goal_distance = math.sqrt((x - goal[0]) ** 2 + (y - goal[1]) ** 2)
                map_grid[x][y] = round(current_distance + goal_distance, 2)
                if map_grid[x][y] < least_val:
                    least_val = map_grid[x][y]
                    path = [x,y]
    print_map(map_grid)

    ## picking short value and removing the rest
    map_grid[path[0]][path[1]] = 'x'
    current = path

    for x, row in enumerate(map_grid):
        for y, value in enumerate(row):
            if isinstance(map_grid[x][y], float):
                map_grid[x][y] = "."
    print_map(map_grid)

    print(current)
    neighbors = []
    for dx, dy in directions:
        neighbor = (current[0] + dx, current[1] + dy)
        neighbors.append(neighbor)