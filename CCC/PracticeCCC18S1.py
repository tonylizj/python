days = int(input())
team1 = input().split(" ")
team2 = input().split(" ")

total1 = 0
total2 = 0
k = 0
for i in range(days):
    total1 += int(team1[i])
    total2 += int(team2[i])

    if total1 == total2:
        k = i + 1

print(k)
