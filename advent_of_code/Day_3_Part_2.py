n = 1000
m = 1000
a = ["."] * n
for i in range(n):
    a[i] = ["."] * m

file = open("Day_3_Input.txt").readlines()

file_parsed = []

for k in file:
    file_parsed.append([k[k.index("@") + 2:k.index(",")], k[k.index(",") + 1:k.index(":")], k[k.index(":") + 2:k.index("x")], k[k.index("x") + 1:-1]])

counter = 0

for j in range(len(file_parsed)):
    for l in range(int(file_parsed[j][1]), int(file_parsed[j][1]) + int(file_parsed[j][3])):
        for m in range(int(file_parsed[j][0]), int(file_parsed[j][0]) + int(file_parsed[j][2])):
            if a[l][m] == ".":
                a[l][m] = "1"

            elif a[l][m] == "1":
                a[l][m] = "X"
                counter += 1

id = 0

for j in range(len(file_parsed)):
    id += 1
    Xcounter = 0

    for l in range(int(file_parsed[j][1]), int(file_parsed[j][1]) + int(file_parsed[j][3])):
        for m in range(int(file_parsed[j][0]), int(file_parsed[j][0]) + int(file_parsed[j][2])):

            if a[l][m] == "X":
                Xcounter += 1

    if Xcounter == 0:
        print(id)
