# 動的計画法
# https://atcoder.jp/contests/typical90/tasks/typical90_ax

N, L = map(int, input().split())
dp = [0]*(N+1)
dp[0] = 1
NUM = 10**9 + 7

for n in range(N):
    dp[n+1] += dp[n]
    dp[n+1] %= NUM
    if n+L <= N:
        dp[n+L] += dp[n]
        dp[n+L] %= NUM

print(dp[N])
