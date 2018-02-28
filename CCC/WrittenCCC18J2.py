size = int(input())
park1 = list(input())
park2 = list(input())

total = 0
for i, slot in enumerate(park1):
    if slot == "C" and park2[i] == "C":
        total += 1

print(total)
