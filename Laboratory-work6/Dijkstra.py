import heapq

def dijkstra(graph, start):
    # graph: словник {u: [(v, w), ...]}
    dist = {v: float("inf") for v in graph}
    pred = {v: None for v in graph}
    dist[start] = 0

    pq = [(0, start)]  # (distance, vertex)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, pred


# Приклад графа з варіанта
graph = {
    1: [(2,8),(3,4),(4,4)],
    2: [(1,8),(3,6),(4,1),(6,6)],
    3: [(1,4),(2,6),(6,3),(8,2)],
    4: [(1,4),(2,1),(5,6)],
    5: [(4,6),(6,5),(7,7)],
    6: [(3,3),(2,6),(5,5),(7,4),(8,4)],
    7: [(5,7),(6,4),(8,5)],
    8: [(3,2),(6,4),(7,5)]
}

distances, predecessors = dijkstra(graph, 1)

print("dist =", distances)
print("pred =", predecessors)
