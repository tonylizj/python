from sys import stdin

input = stdin.readline

n, k = map(int, input().strip().split())

places = list(map(int, input().strip().split()))

mindays = (n//k) + 1
spares = n % k
value = 0

for i in range(mindays-1):
    visits = places[i * k:k * k + k]
    value += max(visits)
    places = places[k + 1:]

print(value)