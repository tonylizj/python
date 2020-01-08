import random
import matplotlib.pyplot


def gamble():
    number = None
    player = 1
    bound = 1000

    while number != 1:
        number = random.randint(1, bound)
        if player == 1:
            player = 2
            bound = number

        else:
            player = 1
            bound = number

    return player


wins = {1: 0, 2: 0}

for i in range(1000000):
    _ = gamble()
    if _ == 1:
        wins[1] += 1

    else:
        wins[2] += 1

for j in range(2):
    matplotlib.pyplot.bar(3*j, wins[j+1], 2)

matplotlib.pyplot.show()