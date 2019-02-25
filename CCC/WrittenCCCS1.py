from sys import stdin

input = stdin.readline

grid = [['1', '2'], ['3', '4']]

flips = list(input())

for i in flips:
    if i == "V":
        grid[0][1], grid[0][0] = grid[0][0], grid[0][1]
        grid[1][1], grid[1][0] = grid[1][0], grid[1][1]

    elif i =="H":
        grid[0], grid[1] = grid[1], grid[0]

print(' '.join(grid[0]))
print(' '.join(grid[1]))
