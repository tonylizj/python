total = 0

for i in range(1, 2019):
    total += (i ** 2) / ((i ** 2) + 1)

for i in range(1, 2019):
    total += ((1/i) ** 2) / (((1/i) ** 2) + 1)

print(total)