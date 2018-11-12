student = []
correct = []
questions = int(input())
numbers = 0

for i in range(questions):
    student.append(input())


for i in range(questions):
    correct.append(input())


for i in range(questions):
    if student[i] == correct[i]:
        numbers += 1

print(numbers)