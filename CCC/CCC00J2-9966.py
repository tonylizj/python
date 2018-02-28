starting = int(input())
end = int(input())

number = ""
total = 0

for i in range(starting, end+1):
    number = str(i)
    newnumber = list(number)
    newnumber.reverse()
    skip = False

    for j in range(len(newnumber)):
        if newnumber[j] in ['2', '3', '4', '5', '7']:
            skip = True

        elif newnumber[j] == '6':
            newnumber[j] = '9'

        elif newnumber[j] == '9':
            newnumber[j] = '6'

    if ''.join(newnumber) == number and not skip:
        total += 1

print(total)