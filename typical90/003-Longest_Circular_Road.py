# https://atcoder.jp/contests/typical90/tasks/typical90_c
# Lv. 4

# 最長経路問題
# bfsを2回やればok

from collections import deque

N = int(input())
road = [[] for _ in range(100001)]
for _ in range(N-1):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)

def bfs(st):
    check = [False] * (N+1)
    rtn_n = st
    rtn_cost = 0
    q = deque([(st, 0)])
    while q:
        #print(q)
        s, cost = q.pop()
        if check[s]:
            continue
        check[s] = True
        for nxt in road[s]:
            if check[nxt]:
                continue
            q.append((nxt, cost + 1))
            if rtn_cost < cost + 1:
                rtn_n = nxt
                rtn_cost = cost + 1
    return (rtn_n, rtn_cost)

mid_n, mid_cost = bfs(1)
_, rtn = bfs(mid_n)

print(rtn + 1)





