# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the grid
N = 100

# Define the initial state of the grid using random function
grid = np.random.choice([0, 1], size=(N, N))

# Define the function to update the grid at each time step
def update(frame_number, grid, N):
    # Copy the grid to avoid overwriting
    new_grid = grid.copy()
    # Loop over each cell in the grid
    for i in range(N):
        for j in range(N):
            # Count the number of live neighbors
            neighbors = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                        grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                        grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                        grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            # Apply the rules of the game
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    # Update the grid
    grid[:] = new_grid[:]
    # Update the plot
    mat.set_data(grid)
    return mat

# Create the animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, fargs=(grid, N), frames=1000, interval=50, save_count=10000)

# Save the animation as a gif
ani.save('life_game.gif', writer='imagemagick')
