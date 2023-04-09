# https://atcoder.jp/contests/typical90/tasks/typical90_h
# Lv 4

# 動的計画法
# n 文字目までで [atcoder (0-6)]文字目まで完成する部分文字列の総数dp[n][0-6]

N = int(input())
S = input()

dic = {"a": 0, "t": 1, "c": 2, "o": 3, "d": 4, "e": 5, "r": 6}
dp = [[0] * 7 for _ in range(N+1)]
for n in range(1, N+1):
    s = S[n-1]
    for m in range(7):
        dp[n][m] = dp[n-1][m]
    if s in dic.keys():
        if s == "a":
            dp[n][dic[s]] += 1
        else:
            dp[n][dic[s]] += dp[n-1][dic[s]-1]
        dp[n][dic[s]] %= 1000000007

print(dp[N][6])


