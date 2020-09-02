from copy import deepcopy
import numpy as np

#input
line1 = input().split()
R, C, N = int(line1[0]), int(line1[1]), int(line1[2])

# we create matrix with zeros
grid = np.zeros((R, C))
# number of starting zeros, later we'll subtract marked locations and thus get output
zeros = R*C


# this function checks for collisions when adding new cell
# with PUT command, while checking if it satisfies border conditions
def collision(row, col, size, f):
    newgrid = deepcopy(grid)
    if row+size > R or col+size > C: return None
    for i in range(row, row+size):
        for j in range(col, col+size):
            if newgrid[i][j] == 0:
                newgrid[i][j] = f
            else: return None
    return newgrid


# This function decides the correct direction according to 'E' 'W' 'N' 'S'
# and moves the cell while checking for collisions
# with other cells or with borders
# in case of collision it returns None
def direction(coord, d, f):
    row, col, size = coord[0], coord[1], coord[2]
    newgrid = deepcopy(grid)

    if d == 'E':
        if col+size == C-1: return None
        else:
            for i in range(row, row+size):
                if grid[i][col+size] != 0: return None
                newgrid[i][col] = 0
                newgrid[i][col+size] = f
    elif d == 'W':
        if col == 0: return None
        else:
            for i in range(row, row+size):
                if grid[i][col - 1] != 0: return None
                newgrid[i][col+size-1] = 0
                newgrid[i][col - 1] = f
    elif d == 'N':
        if row == 0: return None
        else:
            for i in range(col, col+size):
                if grid[row-1][i] != 0: return None
                newgrid[row+size-1][i] = 0
                newgrid[row-1][i] = f
    else:
        if row+size == R-1: return None
        else:
            for i in range(col, col+size):
                if grid[row+size][i] != 0: return None
                newgrid[row][i] = 0
                newgrid[row+size][i] = f

    return newgrid


# f, flag -> all mean flags I marked different cells/blocks with
f = 1
# coordinates is a dictionary to find starting positions for a given point of a block
coordinates = {}
nonzeros = 0

# continue reading input (commands line by line)
for i in range(N):
    command = input().split()
    # actions for command PUT, checks if putting conditions are satisfied:
    # if YES: updates; if NO: does nothing (returns NONE)
    if command[0] == 'P':
        row, col, size = int(command[1]), int(command[2]), int(command[3])
        if grid[row][col] == 0:
            action = collision(row, col, size, f)
            if action is not None:
                # update Grid, number of zeros, flag and dictionary
                # if all PUT conditions are satisfactory
                grid = action
                nonzeros += size*size
                coordinates[f]=[row, col, size]
                f += 1
    # actions for command Move, checks if moving conditions are satisfied:
    # if YES: updates; if NO: does nothing (returns NONE)
    else:
        row, col, d = int(command[1]), int(command[2]), command[3]
        if grid[row][col] != 0:
            flag = grid[row][col]
            action = direction(coordinates[flag], d, flag)
            if action is not None:
                # update Grid, if all MOVE conditions are satisfactory
                grid = action

# output
print(zeros-nonzeros)