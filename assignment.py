"""
-------------------------------------------------------------------------------
Name:		lists_assignment.py
Purpose:    a variety of functions demonstrating knowledge of list processing, list processing with loops, related lists, string methods, and 2D lists.
Author:		Li. T
Created:		27/04/2017
------------------------------------------------------------------------------
"""

# A.1
def unluckyOne(numlist):
    """
    In a given list, returns True if a 1 in the first two or last two positions is immediately followed by a 3. Returns False otherwise.
    :param numlist: list - list to check.
    :return: bool - whether a 1 in the first two or last two positions is immediately followed by a 3.
    """
    # iterates through the list
    for i in range(len(numlist)):
        # returns True if the number is 1 in the first two or last two positions and the number after it is a 3
        if numlist[i] == 1 and i in [0, 1, len(numlist) - 2] and numlist[i+1] == 3:
            return True

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

    # iterates through the list
    for number in numlist:
        # accumulator twos is increased by one if the number is 2
        if number == 2:
            twos += 1

        # accumulator threes is increased by one if the number is 3
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
    # initializes shifted list with the number of elements of the given list
    new_list = [0] * len(numlist)

    # iterates through the list
    for i in range(len(numlist)):
        # shifts every element one index left
        new_list[i - 1] = numlist[i]

    # returns the shifted list
    return new_list


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

    # iterates through the list
    for i in range(len(numlist)):
        # sets seen_multiple as True and store the number if the number is a multiple of ten
        if numlist[i] % 10 == 0:
            seen_multiple = True
            multiple = numlist[i]

        # changes the number to the multiple if seen_multiple is True
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
    :param nums1: list - one of the lists to compare.
    :param nums2: list - another one of the lists to compare.
    :return: int - the number of times when the corresponding numbers of the two lists are not equal but less than three apart.
    """
    # initializes accumulator counts
    counts = 0

    # iterates through one of the lists
    for i in range(len(nums1)):
        # accumulator counts is increased by one if the numbers at the corresponding index are not equal but less than three apart
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
    :param i: int - the number of rows of the grid.
    :param j: int - the number of columns of the grid.
    :return: none.
    """
    # initializes main list
    grid = []

    # iterates through every row
    for y in range(i):
        # appends a nested empty list for every row
        grid.append([])

        # iterates through every element in the row
        for x in range(j):
            # the element is appended as 1 if it is the first row or the first element in the row
            if y == 0 or x == 0:
                grid[y].append(1)

            # the element is appended as the sum of the element above and to the left of it
            else:
                grid[y].append(grid[y][x-1] + grid[y-1][x])

    # iterates through the 2D list for printing
    for y in range(len(grid)):

        for x in range(len(grid[y])):
            # prints the element with a tab and no line break, using the field width of the longest number
            print("{0:<{1}}".format(grid[y][x], len(str(grid[-1][-1]))+2), end="")

        # prints a line break after every row
        print()

print_pascal(10, 10)

# E.2
def diagonal(n):
    """
    With given dimensions, print a square grid of numbers where the diagonal from the top right to the bottom left is 1, numbers above the line is 0, and numbers below the line is 2.
    :param n: the length and width of the printed square grid.
    :return: none.
    """
    # initializes the main list
    grid = []

    # iterates through every row
    for y in range(n):
        # appends a nested empty list for every row
        grid.append([])

        # iterates through every element in the row
        for x in range(n):
            # the element is appended as 1 if is it on the diagonal
            if x == n - y - 1:
                grid[y].append(1)

            # the element is appended as 2 if it is after the 1
            elif x > n - y - 1:
                grid[y].append(2)

            # the element is appended as 0 if it is before the 1
            else:
                grid[y].append(0)

            # prints the element followed by a space without a line break
            print(str(grid[y][x]), end=" ")

        # prints a line break after every row
        print()

diagonal(8)
