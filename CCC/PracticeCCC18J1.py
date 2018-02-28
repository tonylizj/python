number = int(input())

total = 0
hand1 = 0
hand2 = 0

for i in range(number):
    if number <= 5:
        hand1 = number - i
        hand2 = i
        total += 1
        if hand1 == hand2:
            break
        elif hand2 - 1 == hand1:
            total -= 1
            break

    if number > 5:
        hand1 = 5 - i
        hand2 = number - 5 + i
        total += 1
        if hand1 == hand2:
            break
        elif hand2 - 1 == hand1:
            total -= 1
            break

print(total)
