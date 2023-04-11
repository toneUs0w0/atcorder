# https://atcoder.jp/contests/typical90/tasks/typical90_u
# lv 5

# a -> b -> a のパスがあるとき <=> a, bが環状になる
# 強連結成分分解

import sys
sys.setrecursionlimit(10**7) 

N, M = map(int, input ().split())
edges = [[] for _ in range(N + 1)]
rev_edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    rev_edges[b].append(a)

# dfs
check = [False] * (N+1)
indexes = [-1] * (N+1)
index = [1]
def dfs(num):
    check[num] = True
    for nxt in edges[num]:
        if check[nxt]:
            continue
        else:
            dfs(nxt)
            check[nxt] == True
    indexes[num] = index[0]
    index[0] = index[0] + 1

for n in range(1, N + 1):
    if check[n] == False:
        dfs(n)

id_n = []
for n in range(1, N + 1):
    id_n.append((indexes[n], n))
id_n.sort()
id_n.reverse()

#print(id_n)

r_check = [False] * (N+1)
def r_dfs(num):
    #print("start: {}".format(num))
    r_check[num] = True
    child = 0
    for nxt in rev_edges[num]:
        if r_check[nxt]:
            continue
        else:
            child += r_dfs(nxt)
            r_check[nxt] == True
    return child + 1

anses = []
for id, n in id_n:
    if r_check[n] == False:
        anses.append(r_dfs(n))

#print(anses)
ans = 0
for a in anses:
    ans += a * (a-1) // 2

print(ans)

    





