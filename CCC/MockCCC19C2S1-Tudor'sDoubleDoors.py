from decimal import *
getcontext().prec = 100

dimensions = input().split(' ')

print("{:.1f}".format((Decimal(dimensions[0]) * Decimal(dimensions[1])) / 2))