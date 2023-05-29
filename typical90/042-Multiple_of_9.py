# https://atcoder.jp/contests/typical90/tasks/typical90_ap

# Kを(1-9)の和で表す方法は何通りあるか?
# dp[k] kを(1-9)の和で表す方法の総数

K = int(input())
INF = 10**9 + 7

if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K+1)
dp[0] = 1

for k in range(0, K):
    for i in range(1, 10):
        if k + i > K:
            continue
        dp[k+i] += dp[k]
        dp[k+i] %= INF

#print(dp)
print(dp[K])

