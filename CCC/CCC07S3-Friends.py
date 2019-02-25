from sys import stdin

input = stdin.readline


def bfs(g, start, visit, distance):
    seen, queue = [], [start]
    distance[start] = -1

    while queue:
        current = queue.pop(0)

        for adjacent in g[current]:
            if adjacent not in seen:
                seen.append(adjacent)
                queue.append(adjacent)
                distance[adjacent] = distance[current] + 1

        visit.append(current)


graph = {}
separation = {}

people = int(input())

for i in range(1, people + 1):
    graph.update({i: []})
    separation.update({i: 0})

for i in range(people):
    road = list(map(int, input().strip().split(' ')))

    if road[0] not in graph:
        graph[road[0]] = []

    graph[road[0]].append(road[1])

while True:
    conn = list(map(int, input().strip().split(' ')))
    if conn[0] == 0:
        break

    visited = []
    distance = {}

    bfs(graph, conn[0], visited, distance)
    if conn[1] in visited:
        print("Yes {0}".format(distance[conn[1]]))

    else:
        print("No")
