from sys import stdin

input = stdin.readline

visited = []


def bfs(g, root):
    seen, queue = [], [root]
    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)
        for node in g[vertex]:
            if node not in seen:
                seen.append(node)
                queue.append(node)


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