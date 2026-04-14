from grid import create_grid
from pathfinding import astar
from visualization import show_grid

def main():
    grid, start, goal = create_grid()
    
    path = astar(grid, start, goal)
    
    show_grid(grid, start, goal, path)

if __name__ == "__main__":
    main()