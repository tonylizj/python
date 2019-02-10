import sys
from decimal import *
import math
input = sys.stdin.readline
getcontext().prec = 100

coods = input().split(' ')

rope = 0

for i in range(len(coods)):
    coods[i] = Decimal(coods[i])

x = coods[0]
y = coods[1]
x1 = coods[2]
y1 = coods[3]
x2 = coods[4]
y2 = coods[5]


if x1 <= x <= x2:
    if y > y2:
        rope = y - y2

    else:
        rope = y1 - y

elif y1 <= y <= y2:
    if x > x2:
        rope = x - x2

    else:
        rope = x1 - x

else:
    if x > x2:
        if y > y2:
            rope = math.sqrt(((x - x2) ** 2) + (y - y2) ** 2)

        else:
            rope = math.sqrt(((x - x2) ** 2) + (y1 - y) ** 2)

    else:
        if y > y2:
            rope = math.sqrt(((x1 - x) ** 2) + (y - y2) ** 2)

        else:
            rope = math.sqrt(((x1 - x) ** 2) + (y1 - y) ** 2)

print("{0:.3f}".format(rope))