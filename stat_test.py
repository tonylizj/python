n = int(input("n= "))


sum = 0

for k in range(2, n+1):

    inter = 1
    for a in range(1, k):
        inter *= (n-a)

    inter *= (k-1)/((n-1) ** k)

    sum += inter


print(sum)


