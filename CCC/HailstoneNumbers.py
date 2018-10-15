number = int(input())
n = 0
while number != 1:
    if number % 2:
        number = number * 3 + 1

    else:
        number = number / 2

    n += 1

print(n)
