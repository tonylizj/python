villages = []

for i in range(int(input())):
    villages.append(int(input()))

villages.sort()

neighbourhoods = []

for i in range(len(villages)):
    if i != 0:
        neighbourhoods.append((villages[i] - villages[i-1])/2)

neighbourhood_sizes = []

for i in range(len(neighbourhoods)):
    if i != 0:
        neighbourhood_sizes.append(neighbourhoods[i] + neighbourhoods[i-1])

print(float(min(neighbourhood_sizes)))
