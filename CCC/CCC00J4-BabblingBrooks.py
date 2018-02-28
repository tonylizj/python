streams = []
for i in range(int(input())):
    streams.append(int(input()))

while True:
    getInput = int(input())
    if getInput == 99:
        getInput = int(input())
        getFlow = int(input())
        streams = streams[:getInput-1] + [streams[getInput-1] * getFlow/100] + [streams[getInput-1] * (100-getFlow)/100] + streams[getInput:]

    elif getInput == 88:
        getInput = int(input())
        streams = streams[:getInput-1] + [streams[getInput-1] + streams[getInput]] + streams[getInput+1:]

    elif getInput == 77:
        break

for j in range(len(streams)):
    print(int(streams[j]), end=' ')

'''Italian unification success name some people'''
'''italy cant unify itself'''
'''bismarck foreign including unification'''
'''bismarck domestic policy'''