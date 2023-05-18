N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
K = int(input())
Q = []
for _ in range(K):
    p, d = map(int, input().split())
    Q.append((p, d))

ans = [1] * (N + 1)
depth = [[float("Inf")] * (N+1) for _ in range(N+1)]
# 各pに対して距離d未満の全てのマスは白になる

from collections import deque
final = []
for p, d in Q:
    q = deque([(p, 0)])
    check = [False] * (N+1)
    black = []
    while q:
        #print(q)
        st, de = q.pop()
        check[st] = True
        if de == d: #距離d以降はやらない
            black.append(st)
            continue
        if de < d: # 白
            ans[st] = 0
            for nxt in edges[st]:
                if check[nxt]:
                    continue
                else:
                    q.append((nxt, de+1))
                    check[nxt] = True
    final.append(black)

#print(ans)
#print(final)

if 1 not in ans[1:]:
    print("No")
    exit()

for b in final:
    if 1 not in [ans[x] for x in b]:
        print("No")
        exit()

print("Yes")
print("".join([str(x) for x in ans[1:]]))






