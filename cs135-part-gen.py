import random

file = open("cs135-part-testcases.txt", "w")

print("\n\nNOTE: ONLY GENERATES RANDOM TEST CASES, DOES NOT TARGET EDGE CASES!!")
print("ALL TOTAL QUESTION VALUES WILL BE DIVISIBLE BY 4\n")

funcname = input("enter name of function to test: ")
solve = input("should the cases be solved (as a check-within)? True/False ")
maxtotal = int(input("max number of clicker questions allowed: "))

for i in range(int(input("number of cases to generate (rng based so more = better spread): "))):

    total = 1
    while total % 4 != 0:
        total = random.randint(1, maxtotal)

    method = random.randint(0, 1)

    if method == 0:
        correct = random.randint(0, total)
        incorrect = random.randint(0, total - correct)

    else:
        incorrect = random.randint(0, total)
        correct = random.randint(0, total - incorrect)

    if solve:
        totalscore = 2 * 0.75 * total
        if (total - correct - incorrect) >= (0.25 * total):
            score = 100 * (2 * correct + incorrect) / totalscore

        else:
            if incorrect >= ((0.25 * total) - (total - correct - incorrect)):
                incorrect = incorrect - ((0.25 * total) - (total - correct - incorrect))
                score = 100 * (2 * correct + incorrect) / totalscore

            else:
                score = 100

        file.write("(check-within ({} {} {} {}) {} 0.001)\n".format(funcname, total, correct, incorrect, score))

    else:
        file.write("({} {} {} {})\n".format(funcname, total, correct, incorrect))

file.close()

print("test cases generated in current directory :)")
