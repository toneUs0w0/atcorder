# bfs

N, M, K = map(int, input().split())

edge = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
P = []
for _ in range(K):
    p, h = map(int, input().split())
    P.append((h, p))

# hpの高い順にならべる
from collections import deque
save = [False] * (N+1)
P = sorted(P, key=lambda x:x[0])
q = deque([P[0]])
index = 0
while index < len(P):
    q = deque([P[index]])
    index += 1
    while q:
        hp, now = q.popleft()
        if save[now]:
            continue
        while index < len(P) and P[index][0] == hp:
            if save[P[index][1]] == False:
                q.appendleft((P[index]))
            index += 1
        save[now] = True
        for nxt in edge[now]:
            if save[nxt]:
                continue
            q.append((hp-1, nxt))


ans = 0
ans_s = ""
for i in range(1, N+1):
    if save[i]:
        ans += 1
        ans_s += str("{} ".format(i))
print(ans)
print(ans_s)    


