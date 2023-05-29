# https://atcoder.jp/contests/typical90/tasks/typical90_am

# あるパスで二分されるそれぞれの木のsizeの積が、そのパスを通る回数

import sys
sys.setrecursionlimit(10**8)

N = int(input())
edge = [[] for _ in range(N+1)] 
for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

dp = [0 for _ in range(N+1)]
check = [False] * (N+1)

def dfs(pos):
    if check[pos]:
        return
    check[pos] = True
    dp[pos] = 1
    for nxt in edge[pos]:
        if check[nxt]:
            continue
        dfs(nxt)
        dp[pos] += dp[nxt]
 
dfs(1)
ans = 0
for n in range(1, N+1):
    ans += dp[n] * (N - dp[n])

print(ans)



