for i in range(int(input())):
    mountain = []
    branch = []
    counter = 1
    for j in range(int(input())):
        mountain.append(int(input()))

    while True:

        while mountain and mountain[-1] == counter:
            counter += 1
            mountain.pop()

        while branch and branch[-1] == counter:
            counter += 1
            branch.pop()

        while mountain and mountain[-1] != counter and (not branch or branch[-1] != counter):
            branch.append(mountain[-1])
            mountain.pop()

        if not mountain:
            while branch and branch[-1] == counter:
                counter += 1
                branch.pop()

            if not branch:
                print("Y")
                break

            else:
                print("N")
                break
