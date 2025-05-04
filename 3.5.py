import heapq

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        for neighbor, wt in graph[node]:
            new_d = d + wt
            if new_d < dist[neighbor]:
                dist[neighbor] = new_d
                heapq.heappush(pq, (new_d, neighbor))

    print("Shortest distances:", dist)

dijkstra(0)
