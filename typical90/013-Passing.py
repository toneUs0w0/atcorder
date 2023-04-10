# https://atcoder.jp/contests/typical90/tasks/typical90_m
# lv 5
 
# ダイクストラ法っぽい
 
N, M = map(int, input ().split())
Edge = [[] * (N) for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input ().split())
    Edge[a-1].append((c, b-1))
    Edge[b-1].append((c, a-1))
 
import heapq
INF = float("Inf")
 
def dijkstra(edges, start_node: int) -> list:
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    heapq.heappush(hq, (0, start_node))
    dist[start_node] = 0
    # dijkstra
    while hq:
        min_cost, now = heapq.heappop(hq)
        if min_cost > dist[now]:
            continue
        for cost, next in edges[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(hq, (dist[next], next))
    return dist
 
zero_to_k = dijkstra(Edge, 0)
n_to_k = dijkstra(Edge, N-1)
 
for n in range(N):
    print(zero_to_k[n] + n_to_k[n])