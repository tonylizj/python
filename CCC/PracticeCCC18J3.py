import collections

amount = int(input())
sensors = []
for i in range(amount):
    sensors.append(input())

common = collections.Counter(sensors).most_common(2)

print(common)
