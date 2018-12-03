file = open("Day_2_Input.txt")
twice = 0
thrice = 0

for i in range(250):
    line = file.readline().strip()
    letter_list = []
    for j in line:
        letter_list.append(j)

    seen = []
    seenx2 = []
    seenx3 = []
    for k in letter_list:
        if k not in seen:
            seen.append(k)
        elif k in seen and k not in seenx2:
            seenx2.append(k)
        elif k in seen and k in seenx2 and k not in seenx3:
            seenx3.append(k)

    if len(seenx2) - len(seenx3) != 0:
        twice += 1

    if len(seenx3) != 0:
        thrice += 1

file.close()

print(twice * thrice)
