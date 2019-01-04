file = open("Day_4_input.txt").readlines()

file.sort()

n = 934
m = 62
data = ["."] * n
for i in range(n):
    data[i] = ["."] * m

j = 0
current = None
for k, line in enumerate(file):
    if "#" in line:
        if data[j][0] == ".":
            data[j][0] = line[line.index("-") + 1:line.index(" ")]

        else:
            j += 1
            data[j][0] = line[line.index("-") + 1:line.index(" ")]

        data[j][61] = line[line.index("#") + 1:line.index("b") - 1]

    elif "l" in line:
        for l in range(1, 60):
            if int(line[line.index(":") + 1:line.index("]")]) <= l <= int(file[k + 1][file[k + 1].index(":") + 1:file[k + 1].index("]")]):
                data[j][l] = "#"

guards = []
times = []

for m, line in enumerate(data):

    minutes = 0
    for n in range(1, 60):
        if line[n] == "#":
            minutes += 1

    if line[-1] not in guards:
        guards.append(line[-1])
