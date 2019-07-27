alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def fibonacci(n):
    one = 0
    two = 1
    for _ in range(n):
        three = one + two
        one = two
        two = three

    return one


while True:
    letters = list(map(str.lower, list(input())))

    if not letters:
        break

    for i in range(len(letters)):
        try:
            letters[i] = alphabet[alphabet.index(letters[i]) + fibonacci(i + 1)].upper()

        except IndexError:
            letters[i] = alphabet[alphabet.index(letters[i]) + (fibonacci(i + 1) - 26)].upper()

    print(''.join(letters))