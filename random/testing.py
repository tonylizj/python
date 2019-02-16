d = {}
print(d)
d.update({3:4})
print(d)
x = 2
y = 3
d.update({x:y})
print(d)
d.update({2:4})
print(d)
d.update({5:[1]})
print(d)
d.update({5:[2]})
print(d)
d[5].append(3)
print(d)

print(d[3])
for key in d:
    print(key)