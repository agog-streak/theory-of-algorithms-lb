import math

def floyd(W):
    n = len(W)
    # копія для матриці D
    D = [[W[i][j] for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D


# Матриця adjacency (8x8) з варіанта (∞ = велике число)
INF = 10**9

W = [
    [0, 8, 4, 4, INF, INF, INF, INF],
    [8, 0, 6, 1, INF, 6, INF, INF],
    [4, 6, 0, INF, INF, 3, INF, 2],
    [4, 1, INF, 0, 6, INF, INF, INF],
    [INF, INF, INF, 6, 0, 5, 7, INF],
    [INF, 6, 3, INF, 5, 0, 4, 4],
    [INF, INF, INF, INF, 7, 4, 0, 5],
    [INF, INF, 2, INF, INF, 4, 5, 0]
]

D = floyd(W)

print("Матриця Floyd:")
for row in D:
    print(row)
