digit1 = int(input())
digit2 = int(input())
digit3 = int(input())
digit4 = int(input())

if digit1 == 8 or digit1 == 9:
    if digit2 == digit3:
        if digit4 == 8 or digit4 == 9:
            print("ignore")

        else:
            print("answer")

    else:
        print("answer")

else:
    print("answer")
