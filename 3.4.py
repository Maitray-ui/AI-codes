edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
edges.sort(key=lambda x: x[2])

parent = [i for i in range(4)]

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b

mst_weight = 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        mst_weight += w

print("Kruskal's MST Cost:", mst_weight)
