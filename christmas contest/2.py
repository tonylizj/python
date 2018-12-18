size = int(input())

tree = []
for i in range(1, size+1):
    tree.append(((2 * i) - 1)*'*')

field = len(tree[-1])

for j in range(size):
    print(" "*((field - len(tree[j]))//2) + "{0}".format(tree[j]))

print(" "*((field - 3)//2) + "***")