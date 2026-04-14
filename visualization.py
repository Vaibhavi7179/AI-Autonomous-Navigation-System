import matplotlib.pyplot as plt

def show_grid(grid, start, goal, path):
    plt.imshow(grid, cmap='gray')

    if path:
        x, y = zip(*path)
        plt.plot(y, x)

    plt.scatter(start[1], start[0], c='green', label='Start')
    plt.scatter(goal[1], goal[0], c='red', label='Goal')

    plt.legend()
    plt.title("Autonomous Navigation Path")
    plt.show()