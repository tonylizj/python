def checkmonkey(aword):
    if checkaword(aword):
        return True

    elif 'N' in aword:
        nIndex = aword.find('N')
        if nIndex != 0 and aword[-1] != 'N' and checkaword(aword[:nIndex]) and checkmonkey(aword[nIndex + 1:]):
            return True

    else:
        return False


def checkaword(word):
    if word == 'A':
        return True

    elif word[0] == 'B' and word[-1] == 'S':
        return checkmonkey(word[1:-1])

    else:
        return False


while True:
    getInput = input()

    if getInput == 'X':
        break

    if checkmonkey(getInput):
        print("YES")

    else:
        print("NO")