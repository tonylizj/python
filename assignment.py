# A.1
def unluckyOne(numlist):
    """
    In a given list, returns True if a 1 in the first two or last two positions is immediately followed by a 3. Returns False otherwise.
    :param numlist: list - list to check.
    :return: bool - whether a 1 in the first two or last two positions is immediately followed by a 3.
    """
    # possibility means that the last number was a 1 in the first two or last two positions
    possibility = False

    # iterates through every number
    for position, number in enumerate(numlist):
        # set possibility as True if the number is a 1 in the first two or last two positions
        if number == 1 and position in [0, 1, len(numlist) - 1, len(numlist) - 2]:
            possibility = True

        # returns True is the number is 3 and possibility is True
        elif number == 3 and possibility:
            return True

        # set possibility as False if the number is neither
        else:
            possibility = False

    return False


print(unluckyOne([1, 3, 4, 5]))
print(unluckyOne([2, 1, 3, 4, 5]))
print(unluckyOne([1, 1, 1]))


# A.2
def two23(numlist):
    """
    In a given list, returns True if exactly two 2s or 3s are present. Returns False otherwise.
    :param numlist: list - list to check.
    :return: bool - whether exactly two 2s or 3s are present in the list.
    """
    # initializes accumulators twos and threes
    twos = 0
    threes = 0

    # iterates through every number
    for number in numlist:
        # if the number is 2, accumulator twos is increased by one
        if number == 2:
            twos += 1

        # if the number is 3, accumulator threes is increased by one
        elif number == 3:
            threes += 1

    # returns True if either twos or threes refers to 2
    if twos == 2 or threes == 2:
        return True

    return False


print(two23([2, 2]))
print(two23([3, 3]))
print(two23([2, 3]))


# A.3
def shiftLeft3(numlist):
    """
    In a given list with three elements, shift every element left one index. The first element is moved to the end of the list.
    :param numlist: list - list to shift.
    :return: list - a copy of the original list with every element shifted left one index.
    """
    # initializes shifted list with 3 elements
    newlist = [0, 0, 0]

    # iterates through the list
    for i in range(3):
        # shifts every element one index left
        newlist[i - 1] = numlist[i]

    # returns the shifted list
    return newlist


print(shiftLeft3([1, 2, 3]))
print(shiftLeft3([5, 11, 9]))
print(shiftLeft3([7, 0, 0]))


# B.1
def tenStreak(numlist):
    """
    In a given list, change every element after a multiple of ten to that number. When another multiple of ten is encountered, every subsequent element is changed to that number instead. Continues until the end of the list.
    :param numlist: list - list to change.
    :return: list - a copy of the original list with every element after a multiple of ten changed to that number.
    """
    # seen_multiple means a multiple of ten has been found in the list
    seen_multiple = False

    # iterates through every number
    for i in range(len(numlist)):
        # set seen_multiple as True and store the number if the number is a multiple of ten
        if numlist[i] % 10 == 0:
            seen_multiple = True
            multiple = numlist[i]

        # change the number to the multiple if seen_multiple is True
        elif seen_multiple:
            numlist[i] = multiple

    # returns the changed list
    return numlist


print(tenStreak([2, 10, 3, 4, 20, 5]))
print(tenStreak([10, 1, 20, 2]))
print(tenStreak([10, 1, 9, 20]))


# B.2

# B.3

# C.1
def closeby(nums1, nums2):
    """
    In two given lists, returns the number of times when their corresponding numbers are not equal but less than three apart.
    :param nums1: list - one of the lists to compare
    :param nums2: list - one of the lists to compare
    :return: int - the number of times when the corresponding numbers of the two lists are not equal but less than three apart.
    """
    # initializes accumulator counts
    counts = 0

    # iterates through one of the lists
    for i in range(len(nums1)):
        # if the numbers at the corresponding index are not equal but less than three apart, accumulator counts is increased by one
        if nums1[i] != nums2[i] and abs(nums1[i] - nums2[i]) < 3:
            counts += 1

    # returns the number of counts
    return counts


print(closeby([1, 2, 3], [2, 3, 10]))
print(closeby([1, 2, 3], [2, 3, 5]))
print(closeby([1, 2, 3], [2, 3, 3]))


# C.2

# D.1
def loudVowels(sentence):
    """
    In a given string, return a copy of the original with every vowel (a, e, i, o, u) capitalized.
    :param sentence: str - the text to change.
    :return: str - a copy of the original with every vowel capitalized.
    """
    # changes the string to a list of letters
    sentence_list = list(sentence)

    # iterates through the list
    for i in range(len(sentence_list)):
        # changes the letter to its uppercase when a vowels is found
        if sentence_list[i] in ["a", "e", "i", "o", "u"]:
            sentence_list[i] = sentence_list[i].upper()

    # returns the list joined like its original string
    return "".join(sentence_list)


print(loudVowels("I snap my fingers when I sing"))


# D.2

# E.1
def print_pascal(i, j):
    """
    With given length and width, print a grid of numbers according to pascal's triangle where every number is the sum of the number above and to the left of it.
    :param i: int - the number of rows of the grid
    :param j: int - the number of columns of the grid
    :return: none
    """
    # initializes main list
    triangle = []

    # iterates through every row
    for y in range(i):
        # append a nested list for every row
        triangle.append([])
        # iterates through every element in the row
        for x in range(j):
            # every element is set as 1 if it is the first row
            if y == 0:
                triangle[y].append(1)

            # the element is set as 1 if it is the first element in the row
            elif x == 0:
                triangle[y].append(1)

            # the element is set as the sum of the element above and to the left of it
            else:
                triangle[y].append(triangle[y][x-1] + triangle[y-1][x])

            # prints the element with a tab and no line break
            print(str(triangle[y][x]) + "\t", end='')

        # at the end of every row, print a line break
        print("")

print_pascal(3,4)

# E.2
