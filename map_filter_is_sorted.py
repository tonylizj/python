a = [5, 7, 8, 13, 22, 60]


def is_sorted(lst):
    return list(map(lambda x: list(filter(lambda y: y < x, lst)), lst)) == list(map(lambda z: lst[:z], range(len(lst))))


print(is_sorted(a))
