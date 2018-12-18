import math
base = input().split(' ')

for i in range(3):
    base[i] = int(base[i])

counter = 0

for j in range(3):
    star = input().split(' ')
    if math.sqrt((int(star[0]) - int(base[1])) ** 2 + (int(star[1]) - int(base[2])) ** 2 ) < int(base[0]):
        counter += 1

if counter == 3:
    print("YES")

else:
    print("NO")