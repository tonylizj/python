flowers = int(input())

data = []

for i in range(flowers):
    data.append(input().split(" "))

def uprightcheck(recording, amount):
    recordingver = []
    for j in range(amount):
        newrecording = list(recording[j])
        newrecording.sort()
        print(recording[j])
        print(newrecording)

        if recording[j] == newrecording:
            continue

        else:
            return False

    for k in range(amount):
        recordingver.append(recording[k][0])

    newrecordingver = recordingver[0:]
    newrecordingver.sort()
    print(recordingver)
    print(newrecordingver)

    if recordingver == newrecordingver:
        return True

    else:
        return False

turns = 0
while turns != 4:
    newdata = []

    chunk = []

    for l in range(flowers):
        for m in range(flowers):
            chunk.append(data[l][-1])

        newdata.append(chunk)

    if not uprightcheck(data, flowers):
        data = newdata
        continue

    else:
        for n in range(flowers):
            for o in range(flowers):
                print(data[n][o], end=" ")

        print()
