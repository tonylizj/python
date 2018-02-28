starting = input()
total = int(starting[2:])
starting = int(starting[0])
print("Sun Mon Tue Wed Thr Fri Sat")
for i in range(starting-1):
    print("   ", end=' ')

for i in range(total):
    if (i+starting) % 7 != 0 and i+1 != total:
        print("{0:>3d}".format(i+1), end=' ')
    else:
        print("{0:>3d}".format(i + 1))