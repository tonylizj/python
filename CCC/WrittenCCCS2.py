from sys import stdin
import math

input = stdin.readline


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for k in range(3, sqrt_n + 1, 2):
        if n % k == 0:
            return False
    return True


for j in range(int(input())):
    number = 2 * int(input())
    for i in range(3, (number//2) + 1, 2):

        if is_prime(i) and is_prime(number - i):
            print(str(i) + " " + str(int(number-i)))
            break

