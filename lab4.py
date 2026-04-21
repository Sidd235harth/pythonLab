import heapq
import matplotlib.pyplot as plt

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.parent = None
        self.g_value = float('inf')
        self.h_value = 0

    def __lt__(self, other):
        return (self.g_value + self.h_value) < (other.g_value + other.h_value)

def a_star(grid, start, goal):
    start_cell = Cell(start[0], start[1])
    goal_cell = Cell(goal[0], goal[1])

    open_list = []
    heapq.heappush(open_list, start_cell)

    closed_list = set()
    nodes = {(start_cell.row, start_cell.col): start_cell}

    start_cell.g_value = 0
    start_cell.h_value = abs(start_cell.row - goal_cell.row) + abs(start_cell.col - goal_cell.col)

    while open_list:
        current_cell = heapq.heappop(open_list)

        if current_cell.row == goal_cell.row and current_cell.col == goal_cell.col:
            path = []
            while current_cell:
                path.append((current_cell.row, current_cell.col))
                current_cell = current_cell.parent
            path.reverse()
            return path

        closed_list.add((current_cell.row, current_cell.col))

        for d_row, d_col in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor_row = current_cell.row + d_row
            neighbor_col = current_cell.col + d_col

            if not (0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0])):
                continue
            if grid[neighbor_row][neighbor_col] == 0:
                continue
            if (neighbor_row, neighbor_col) in closed_list:
                continue

            if (neighbor_row, neighbor_col) not in nodes:
                neighbor_cell = Cell(neighbor_row, neighbor_col)
                nodes[(neighbor_row, neighbor_col)] = neighbor_cell
            else:
                neighbor_cell = nodes[(neighbor_row, neighbor_col)]

            tentative_g_value = current_cell.g_value + 1

            if tentative_g_value < neighbor_cell.g_value:
                neighbor_cell.parent = current_cell
                neighbor_cell.g_value = tentative_g_value
                neighbor_cell.h_value = abs(neighbor_row - goal_cell.row) + abs(neighbor_col - goal_cell.col)
                heapq.heappush(open_list, neighbor_cell)

    return []

grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)
print("Shortest path:", path)

plt.imshow(grid, cmap='gray')
plt.colorbar()

plt.plot(start[1], start[0], 'bo', markersize=10)
plt.plot(goal[1], goal[0], 'ro', markersize=10)

if path:
    path_row, path_col = zip(*path)
    plt.plot(path_col, path_row, 'g-', linewidth=3)

plt.gca().invert_yaxis()
plt.show()
