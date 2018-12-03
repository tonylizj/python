number = 0
file = open("Day_1_Input.txt")
already_list = []
changes = []

for i in range(1011):
    changes.append(file.readline().strip())

file.close()

counter = 0

while True:
    try:
        number += int(changes[counter])
    except IndexError:
        counter = 0
        continue
    if number in already_list:
        print(number)
        break
    already_list.append(number)
    counter += 1
