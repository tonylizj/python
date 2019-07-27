print("Shifts input number of keys left or right.")
print("Type: typeshift(\"your word\", the number of keys to shift right (use negatives to shift left))\n")
print("For example:\n\ntypeshift(\"wait\", -1)\n=> 'qlur'")


def typeshift(string, shift):
    """
    Shifts input number of keys left or right.
    Type: typeshift(\"your word\", the number of keys to shift right (use negatives to shift left))

    For example:
    typeshift("wait", -1)
    => 'qlur'

    Only works on QWERTY keyboards
    """

    # sets keys on each line of keyboard and converts string to list of letters
    keyboard = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"], ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                ["z", "x", "c", "v", "b", "n", "m"]]
    string_list = list(string.lower())

    # iterates through list of letters
    for i in range(len(string_list)):

        # if the letter is in the top row
        if string_list[i] in keyboard[0]:

            # shifts the letter based on the number of keys to shift
            try:
                string_list[i] = keyboard[0][keyboard[0].index(string_list[i]) + shift]

            # if the letter is shifted past the keyboard, continue shifting from the other side
            except IndexError:
                string_list[i] = keyboard[0][keyboard[0].index(string_list[i]) + (shift - len(keyboard[0]))]

        # if the letter is in the middle row
        if string_list[i] in keyboard[1]:

            # shifts the letter based on the number of keys to shift
            try:
                string_list[i] = keyboard[1][keyboard[1].index(string_list[i]) + shift]

            # if the letter is shifted past the keyboard, continue shifting from the other side
            except IndexError:
                string_list[i] = keyboard[1][keyboard[1].index(string_list[i]) + (shift - len(keyboard[1]))]

        # if the letter is in the bottom row
        if string_list[i] in keyboard[2]:

            # shifts the letter based on the number of keys to shift
            try:
                string_list[i] = keyboard[2][keyboard[2].index(string_list[i]) + shift]

            # if the letter is shifted past the keyboard, continue shifting from the other side
            except IndexError:
                string_list[i] = keyboard[2][keyboard[2].index(string_list[i]) + (shift - len(keyboard[2]))]

    # returns the joined list
    return "".join(string_list)
