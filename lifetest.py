import random
import matplotlib.pyplot


def lifetest(times):
    stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for i in range(times):
        counter = 0
        while counter < 150:
            r = random.randint(1, 10)
            stats[r] += 1
            counter += r

    return stats


plot = lifetest(33000)
for j in range(10):
    matplotlib.pyplot.bar(10*j, plot[j+1], 9)
matplotlib.pyplot.show()
