import sys
input = sys.stdin.readline
from itertools import combinations

posts = []

n = int(input())

for i in range(n):
    posts.append(tuple(map(int, input().strip().split(' '))))

pens = tuple(combinations(posts, 3))
length = len(pens)

impossibles = 0

for i in range(length):
    if pens[i][0][0] * pens[i][1][1] + pens[i][1][0] * pens[i][2][1] + pens[i][2][0] * pens[i][0][1] == \
            pens[i][1][0] * pens[i][0][1] + pens[i][2][0] * pens[i][1][1] + pens[i][0][0] * pens[i][2][1]:
        impossibles += 1

print(length - impossibles)
