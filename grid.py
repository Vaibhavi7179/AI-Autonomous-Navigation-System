import numpy as np

def create_grid():
    grid = np.zeros((10, 10))

    # obstacles
    grid[3, 4] = 1
    grid[3, 5] = 1
    grid[4, 5] = 1
    grid[5, 5] = 1

    start = (0, 0)
    goal = (9, 9)

    return grid, start, goal