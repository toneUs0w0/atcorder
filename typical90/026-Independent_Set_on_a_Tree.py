# https://atcoder.jp/contests/typical90/tasks/typical90_z
# lv 4

# 深さ優先探索で深さが奇数または偶数のノードを全て取り出す
# 奇/偶どちらかはN/2以上になるので, 超えた方をN/2個だけ取り出せば良い

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

from collections import deque

def bfs(st):
    nest = [0] * (N+1)
    q = deque([(st, 1)])
    while q:
        now, nst = q.pop()
        if nest[now] != 0:
            continue
        nest[now] = nst
        for nxt in edges[now]:
            if nest[nxt] != 0:
                continue
            q.append((nxt, nst + 1))
    return nest

deep = bfs(1)
ans = []
ans2 = []
for n in range(1, N + 1):
    if deep[n] % 2 == 1:
        ans.append(n)
    else:
        ans2.append(n)
    if len(ans) == N // 2:
        print(" ".join([str(a) for a in ans]))
        exit()
    if len(ans2) == N // 2:
        print(" ".join([str(a) for a in ans2]))
        exit()

