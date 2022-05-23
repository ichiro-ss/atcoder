import heapq
# input
n, m = [int(_) for _ in input().split()]
G = [[] for _ in range(n)]
for i in range(m):
    a, b, c = [int(_) for _ in input().split()]
    G[a-1].append([b-1, c, i])
    G[b-1].append([a-1, c, i])

INF = 10 ** 18

def dijkstra(s, glaph):
    dist = [INF for _ in range(n)]
    dist[0] = 0
    last_path = [0 for _ in range(n)]

    que = []
    heapq.heappush(que, (0, s))
    while que:
        d, v  = heapq.heappop(que)
        if dist[v] < d:
            continue
        for v2, c, i in G[v]:
            if dist[v] + c < dist[v2]:
                dist[v2] = dist[v] + c
                heapq.heappush(que, (dist[v2], v2))
                last_path[v2] = i
    return last_path

ans = dijkstra(0, G)
for i in range(1, n):
    print(ans[i] + 1, end=" ")
