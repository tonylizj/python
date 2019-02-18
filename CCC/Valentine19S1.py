from sys import stdin

input = stdin.readline

dimensions = list(map(int, input().strip().split(' ')))

candidates = {}
voters = {}

for i in range(dimensions[0]):
    candidates[input().strip()] = 0

for i in range(dimensions[1]):
    voters[i] = input().strip().split(' ')

for voter in voters:
    candidates[voters[voter][1]] += 1

done = False

while not done:
    minimumv = 10001
    minimumk = None
    for candidate in candidates:
        if candidates[candidate] < minimumv:
            minimumv = candidates[candidate]
            minimumk = candidate

    candidates.pop(minimumk, None)

    topop = []

    for voter in voters:
        if minimumk in voters[voter]:
            if minimumk == voters[voter][1]:
                if voters[voter][0] == 1 or voters[voter][0] == '1':
                    topop.append(voter)

                else:
                    if voters[voter][2] in candidates:
                        candidates[voters[voter][2]] += 1

            voters[voter].remove(minimumk)
            voters[voter][0] = int(voters[voter][0]) - 1

    for v in topop:
        voters.pop(v)

    if len(candidates) == 1:
        for candidate in candidates:
            print(candidate)
            done = True
