from sys import stdin

input = stdin.readline


def bfs(g, start, visit):
    seen, queue = [], [start]
    while queue:
        vertex = queue.pop(0)

        for node in g[vertex]:
            if node not in seen:
                seen.append(node)
                queue.append(node)

        visit.append(vertex)


graph = {}
separation = {}

people = int(input())

for i in range(1, people + 1):
    graph.update({i: []})
    separation.update({i: 0})

for i in range(people):
    road = list(map(int, input().strip().split(' ')))

    graph[road[0]].append(road[1])

while True:
    conn = list(map(int, input().strip().split(' ')))
    if conn[0] == 0:
        break

    visited = []

    bfs(graph, conn[0], visited)
    if conn[1] in visited:
        print("Yes {0}".format(distance))

    else:
        print("No")
