def prim_mst(graph):
    import heapq

    n = len(graph)
    start = 1

    used = [False] * (n + 1)
    mst = []
    total_weight = 0

    pq = []
    used[start] = True

    # Додаємо всі ребра зі стартової вершини
    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq and len(mst) < n - 1:
        w, u, v = heapq.heappop(pq)

        if used[v]:
            continue

        used[v] = True
        mst.append((u, v, w))
        total_weight += w

        for to, weight in graph[v]:
            if not used[to]:
                heapq.heappush(pq, (weight, v, to))

    return mst, total_weight


# --- Граф твого варіанта ---
graph = {
    1: [(2, 8), (3, 4), (4, 4)],
    2: [(1, 8), (4, 1), (6, 6)],
    3: [(1, 4), (6, 3), (8, 2)],
    4: [(1, 4), (2, 1), (5, 6)],
    5: [(4, 6), (6, 5), (7, 7)],
    6: [(2, 6), (3, 3), (5, 5), (7, 4)],
    7: [(5, 7), (6, 4), (8, 5)],
    8: [(3, 2), (7, 5)],
}

mst, total = prim_mst(graph)

print("MST Пріма:")
for u, v, w in mst:
    print(f"{u} - {v} (w={w})")
print("Сумарна вага:", total)
