number = int(input())
shifts = int(input())

newnumber = number
for i in range(shifts):
    newnumber += number * (10**(i+1))

print(newnumber)