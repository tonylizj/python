"""
-------------------------------------------------------------------------------
Name:		fun_translator.py
Purpose:
translates a given text file to pirate

Author:		Li.T

Created:		22/05/2017
------------------------------------------------------------------------------
"""

# opens the source text for reading and makes/opens for writing the translated file
text = open("source.txt", "r")
output = open("translated.txt", "w")

# converts the source text into a list of every letter
text_list = list(text.read())

# iterates through the list
for i in range(len(text_list)):

    # changes "Yes" to "Aye", changes "yes" to "aye"
    if text_list[i] == "s" and text_list[i-1] == "e" and text_list[i-2] == "Y" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Aye"
        text_list[i-1] = ""
        text_list[i-2] = ""

    elif text_list[i] == "s" and text_list[i-1] == "e" and text_list[i-2] == "y" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "aye"
        text_list[i-1] = ""
        text_list[i-2] = ""

    # changes "Not" and "No" to "Nay, changes "not" and "no" to "nay"
    elif text_list[i] == "t" and text_list[i-1] == "o" and text_list[i-2] == "n" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "nay"
        text_list[i-1] = ""
        text_list[i-2] = ""

    elif text_list[i] == "t" and text_list[i-1] == "o" and text_list[i-2] == "N" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Nay"
        text_list[i-1] = ""
        text_list[i-2] = ""

    elif text_list[i] == "o" and text_list[i-1] == "N" and text_list[i-2] == " " and text_list[i+1] not in ["t", "T"]:
        text_list[i] = "Nay"
        text_list[i-1] = ""

    elif text_list[i] == "o" and text_list[i-1] == "n" and text_list[i-2] == " " and text_list[i+1] not in ["t", "T"]:
        text_list[i] = "nay"
        text_list[i-1] = ""

    # changes "Wine" and "Beer" to "Grog", changes "wine" and "beer" to grog"
    elif text_list[i] == "e" and text_list[i-1] == "n" and text_list[i-2] == "i" and text_list[i-3] == "w" and text_list[i-4] == " ":
        text_list[i] = "grog"
        text_list[i-1] = ""
        text_list[i-2] = ""
        text_list[i-3] = ""

    elif text_list[i] == "e" and text_list[i-1] == "n" and text_list[i-2] == "i" and text_list[i-3] == "W" and text_list[i-4] == " ":
        text_list[i] = "Grog"
        text_list[i-1] = ""
        text_list[i-2] = ""
        text_list[i-3] = ""

    elif text_list[i] == "r" and text_list[i-1] == "e" and text_list[i-2] == "e" and text_list[i-3] == "b" and text_list[i-4] == " ":
        text_list[i] = "grog"
        text_list[i-1] = ""
        text_list[i-2] = ""
        text_list[i-3] = ""

    elif text_list[i] == "r" and text_list[i-1] == "e" and text_list[i-2] == "e" and text_list[i-3] == "B" and text_list[i-4] == " ":
        text_list[i] = "Grog"
        text_list[i-1] = ""
        text_list[i-2] = ""
        text_list[i-3] = ""

    # adds "Yarr!" after every sentence
    elif text_list[i] == " " and text_list[i-1] == ".":
        text_list[i] = " Yarr! "

    elif text_list[i] == "\n" and text_list[i-1] == ".":
        text_list[i] = " Yarr!\n"

    # changes "You" to "Ye", changes "you" to "ye"
    elif text_list[i] == "u" and text_list[i-1] == "o" and text_list[i-2] == "Y" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Ye"
        text_list[i-1] = ""
        text_list[i-2] = ""

    elif text_list[i] == "u" and text_list[i-1] == "o" and text_list[i-2] == "y" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "ye"
        text_list[i-1] = ""
        text_list[i-2] = ""

    # changes every form of (caps) "To Be" to "Be", changes every form of "to be" to "be:
    elif text_list[i] == "e" and text_list[i-1] == "r" and text_list[i-2] == "A" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Be"
        text_list[i-1] = ""
        text_list[i-2] = ""

    elif text_list[i] == "e" and text_list[i-1] == "r" and text_list[i-2] == "a" and text_list[i-3] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "be"
        text_list[i-1] = ""
        text_list[i-2] = ""

    elif text_list[i] == "s" and text_list[i-1] == "I" and text_list[i-2] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Be"
        text_list[i-1] = ""

    elif text_list[i] == "s" and text_list[i-1] == "i" and text_list[i-2] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "be"
        text_list[i-1] = ""

    elif text_list[i] == "m" and text_list[i-1] == "A" and text_list[i-2] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Be"
        text_list[i-1] = ""

    elif text_list[i] == "m" and text_list[i-1] == "a" and text_list[i-2] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "be"
        text_list[i-1] = ""

    # changes "a" to "an"
    elif text_list[i] == "a" and text_list[i+1] == " " and text_list[i-1] == " ":
        text_list[i] = "an"

    # changes "Hi" and "Hello" to "Ahoy", changes "hi" and "hello" to "ahoy"
    elif text_list[i] == "i" and text_list[i-1] == "H" and text_list[i-2] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Ahoy"
        text_list[i-1] = ""

    elif text_list[i] == "i" and text_list[i-1] == "h" and text_list[i-2] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "ahoy"
        text_list[i-1] = ""

    elif text_list[i] == "o" and text_list[i-1] == "l" and text_list[i-2] == "l" and text_list[i-3] == "e" and text_list[i-4] == "h" and text_list[i-5] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "ahoy"
        text_list[i-1] = ""
        text_list[i-2] = ""
        text_list[i-3] = ""
        text_list[i-4] = ""

    elif text_list[i] == "o" and text_list[i-1] == "l" and text_list[i-2] == "l" and text_list[i-3] == "e" and text_list[i-4] == "H" and text_list[i-5] == " " and text_list[i+1] in [" ", "\n", ".", ",", "!", "?"]:
        text_list[i] = "Ahoy"
        text_list[i-1] = ""
        text_list[i-2] = ""
        text_list[i-3] = ""
        text_list[i-4] = ""

    # duplicates every "r" and "R"
    if text_list[i] == "r" and (text_list[i-1] != "rr" or text_list[i-1] != "RR"):
        text_list[i] = "rr"

    if text_list[i] == "R" and (text_list[i-1] != "rr" or text_list[i-1] != "RR"):
        text_list[i] = "RR"

    # changes every "s" to "th"
    if text_list[i] == "s":
        text_list[i] = "th"

# writes the joined version of the changes list to "translated.txt"
output.write("".join(text_list))

# closes both files
text.close()
output.close()
