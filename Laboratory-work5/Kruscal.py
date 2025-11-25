def kruskal_mst(graph):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            if u < v:          # уникаємо дублювання (бо граф неорієнтований)
                edges.append((w, u, v))

    edges.sort()

    parent = {}
    rank = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

    # Ініціалізація множин
    for v in graph:
        parent[v] = v
        rank[v] = 0

    mst = []
    total_weight = 0

    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


# Той самий граф
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

mst, total = kruskal_mst(graph)

print("MST Крускала:")
for u, v, w in mst:
    print(f"{u} - {v} (w={w})")
print("Сумарна вага:", total)
