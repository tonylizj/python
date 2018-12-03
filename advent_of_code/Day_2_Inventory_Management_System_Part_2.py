file = open("Day_2_Input.txt")
lines = file.readlines()
file.close()

for i in range(250):
    current = list(lines[i])[:-1]

    for j in range(i + 1, 250 - i):
        new = list(lines[j])[:-1]

        samechars = []
        for k in range(26):
            if current[k] == new[k]:
                samechars.append(new[k])

        if len(samechars) == 25:
            print("".join(samechars))
            break
