graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

def dfs(v, visited=set()):
    if v not in visited:
        print(v, end=' ')
        visited.add(v)
        for n in graph[v]:
            dfs(n, visited)

def bfs(start):
    visited = set()
    queue = [start]
    while queue:
        v = queue.pop(0)
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            queue.extend(graph[v])

print("DFS:")
dfs(0)
print("\nBFS:")
bfs(0)
