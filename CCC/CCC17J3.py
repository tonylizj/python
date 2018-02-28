firstcood = input()
secondcood = input()
charge = int(input())

firstcood = firstcood.split(" ")
secondcood = secondcood.split(" ")

firstx = int(firstcood[0])
firsty = int(firstcood[1])
secondx = int(secondcood[0])
secondy = int(secondcood[1])

distance = abs(secondx - firstx) + abs(secondy - firsty)

if charge < distance:
    print("N")

elif (charge - distance) % 2 == 0:
    print("Y")

else:
    print("N")