from sys import stdin

input = stdin.readline

visited = []


def bfs(g, start):
    seen, queue = [start], [start]

    while queue:
        current = queue.pop(0)

        for adjacent in g[current]:
            if adjacent not in seen:
                seen.append(adjacent)
                queue.append(adjacent)

        visited.append(current)


graph = {}

outline = list(map(int, input().strip().split(' ')))

for i in range(1, outline[0] + 1):
    graph.update({i: []})

for i in range(outline[1]):
    road = list(map(int, input().strip().split(' ')))

    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0])

bfs(graph, outline[2])

if outline[3] in visited:
    print("GO SHAHIR!")

else:
    print("NO SHAHIR!")