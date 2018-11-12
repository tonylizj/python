start = input().split(' ')
end = input().split(' ')

charge = int(input())

ydiff = abs(int(end[-1]) - int(start[-1]))
xdiff = abs(int(end[0]) - int(start[0]))

totaldiff = ydiff + xdiff

if charge < totaldiff:
    print("N")

elif (totaldiff - charge) % 2 == 0:
    print("Y")

else:
    print("N")