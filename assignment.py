# A.1
def unluckyOne(numlist):
    """

    :param numlist:
    :return: bool
    """
    possibility = False
    for position, number in enumerate(numlist):
        if number == 1 and position in [0, 1, len(numlist) - 1, len(numlist) - 2]:
            possibility = True

        elif number == 3 and possibility:
            return True

        else:
            possibility = False

    return False


print(unluckyOne([1, 3, 4, 5]))
print(unluckyOne([2, 1, 3, 4, 5]))
print(unluckyOne([1, 1, 1]))




# A.2
def two23(numlist):
    twos = 0
    threes = 0
    for number in numlist:
        if number == 2:
            twos += 1

        elif number == 3:
            threes += 1

    if twos == 2 or threes == 2:
        return True

    return False


print(two23([2, 2]))
print(two23([3, 3]))
print(two23([2, 3]))


# A.3
def shiftLeft3(numlist):
    newlist = [0, 1, 2]
    for i in range(len(numlist)):
        newlist[i - 1] = numlist[i]

    return newlist


print(shiftLeft3([1, 2, 3]))
print(shiftLeft3([5, 11, 9]))
print(shiftLeft3([7, 0, 0]))


# B.1
def tenStreak(numlist):
    seen_multiple = False
    for i in range(len(numlist)):
        if numlist[i] % 10 == 0:
            seen_multiple = True
            multiple = numlist[i]

        elif seen_multiple:
            numlist[i] = multiple

            # else:
            # continue

    return numlist


print(tenStreak([2, 10, 3, 4, 20, 5]))
print(tenStreak([10, 1, 20, 2]))
print(tenStreak([10, 1, 9, 20]))


# B.2

# B.3

# C.1
def closeby(nums1, nums2):
    counts = 0
    for i in range(len(nums1)):
        if nums1[i] != nums2[i] and abs(nums1[i] - nums2[i]) < 3:
            counts += 1

    return counts


print(closeby([1, 2, 3], [2, 3, 10]))
print(closeby([1, 2, 3], [2, 3, 5]))
print(closeby([1, 2, 3], [2, 3, 3]))


# C.2

# D.1
def loudVowels(sentence):
    sentence_list = list(sentence)
    for i in range(len(sentence_list)):
        if sentence_list[i] in ["a", "e", "i", "o", "u"]:
            sentence_list[i] = sentence_list[i].upper()

    return "".join(sentence_list)


print(loudVowels("I snap my fingers when I sing"))
