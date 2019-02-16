from sys import stdin

input = stdin.readline

n = list(map(int, input().strip().split(' ')))

g = [[0 for i in range(n[0])] for j in range(n[0])]

for i in range(n[1]):
    _ = list(map(int, input().strip().split(' ')))
    _[1] = _[1] - 1
    _[2] = _[2] - 1
    if _[0] == 1:
        for y in range(n[0]):
            for x in range(n[0]):
                if (y == _[2] and x != _[1]) or (x == _[1] and y != _[2]):
                    if g[y][x] == 0:
                        g[y][x] = 1

                    else:
                        g[y][x] = 0

                if y == _[2] and x == _[1]:
                    if g[y][x] == 0:
                        g[y][x] = 1

                    else:
                        g[y][x] = 0

    else:
        print(g[_[2]][_[1]])
