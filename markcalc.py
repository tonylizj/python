def mark(listoflist):
    weighttotal = 0
    marktotal = 0
    for test in listoflist:
        weighttotal += test[0]
        marktotal += test[1] * test[0]

    return marktotal / weighttotal


tests = [

    [35, 97.1],
    [37, 98.6],
    [40, 96.3],
    [42, 97.6],
    [38, 98.7],
    [43, 97.7],
    [42, 88.1],
    [30, 98.3],
    [21, 97.6],
]

print(mark(tests))
