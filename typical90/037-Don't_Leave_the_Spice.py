#  https://atcoder.jp/contests/typical90/tasks/typical90_ak

# 選択した料理の sum_L <= W <= sum_R であれば良い

# ナップサック → 動的計画法

#dp[参照した料理][香辛料の合計] = 価値の合計の最大値

from collections import deque

W, N = map(int, input().split())
LRV = []
for _ in range(N):
    LRV.append(tuple(map(int, input().split())))

INF = 10**18
dp = [[-INF] * (W+1) for _ in range(N+1)]

dp[0][0] = 0

for i in range(1, N+1):
    l, r, v = LRV[i-1]
    q = deque()
    nxt = 0
    # 事前にmax(dp[i-1][j-k])を求めておく
    for j in range(W+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])  # 料理iを作らない場合

        # 料理iを作る場合は l <= k <= r である k について max(dp[i-1][j-k]) + v[i]に更新
        window_r = j - l
        window_l = j - r
        #print("{}, {}".format(window_l, window_r))
        while nxt <= window_r:
            while len(q) > 0 and q[-1][0] < dp[i-1][nxt]:
                q.pop()
            q.append((dp[i-1][nxt], nxt))
            #print(q)
            nxt += 1

        while len(q) > 0 and q[0][1] < window_l:
            q.popleft()
            #print(q)
        if len(q) <= 0:
            continue
        dp[i][j] = max(dp[i][j], q[0][0] + v)

if dp[N][W] < 0:
    print(-1)
else:
    print(dp[N][W])
        





