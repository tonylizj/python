distances = input().split(" ")
for i in range(len(distances)):
    distances[i] = int(distances[i])

newdistances = []

for i in range(5):
    newdistances.append([])

newdistances[0].append(0)
newdistances[0].append(distances[0])
newdistances[0].append(distances[0] + distances[1])
newdistances[0].append(distances[0] + distances[1] + distances[2])
newdistances[0].append(distances[0] + distances[1] + distances[2] + distances[3])

for i in range(5):
    for j in range(5):
        if j == i and i != 0:
            newdistances[i].append(0)

        elif j < i and i != 0:
            newdistances[i].append(newdistances[i-1][j] + distances[i-1])

        elif i < j and i != 0:
            newdistances[i].append(newdistances[i-1][j] - distances[i-1])

        print(newdistances[i][j], end=" ")

    print()
