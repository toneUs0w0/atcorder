# union-find
N, M = map(int, input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)
K = int(input())
good = []
for _ in range(K):
    good.append(tuple(map(int, input().split())))
Q = int(input())
query = []
for _ in range(Q):
    query.append(tuple(map(int, input().split())))


