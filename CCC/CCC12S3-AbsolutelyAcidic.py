from sys import stdin

input = stdin.readline

readings = {}

for i in range(int(input())):
    _ = int(input())
    if _ in readings:
        readings[_] += 1

    else:
        readings[_] = 1

prevmax = 0
prevr = []
m = 0
multi = 0
r = []

for j in readings:
    if prevmax < readings[j] < m:
        prevmax = readings[j]
        prevr = [j]

    if readings[j] > m:
        prevmax = m
        m = readings[j]
        multi = 1
        prevr = r
        r = [j]

    elif readings[j] == m:
        multi += 1
        r.append(j)

if multi > 1:
    print(abs(max(r) - min(r)))

else:
    print(abs(r[0] - prevr[0]))
