import heapq

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

def prim(start):
    visited = set()
    heap = [(0, start)]
    total_cost = 0

    while heap:
        weight, node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            total_cost += weight
            for neighbor, wt in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (wt, neighbor))

    print("Prim's MST Cost:", total_cost)

prim(0)
