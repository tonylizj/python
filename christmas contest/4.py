base = input().split()

for i in range(len(base)):
    base[i] = int(base[i])

fav = []
des = []

for j in range(base[0]):
    guest = input().split()
    fav.append(int(guest[0]))
    des.append(int(guest[1]))

changes = 0
begin = base[2]

while True:
    if base[2] not in des:
        print(changes)
        break

    else:
        base[2] = fav[des.index(base[2])]
        changes += 1

    if base[2] == begin:
        print(-1)
        break
