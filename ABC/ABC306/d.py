

N = int(input())
menu = []
for _ in range(N):
    x, y = map(int, input().split())
    menu.append((x, y))

dp = [[-float('Inf'), -float('Inf')] for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = 0

for i in range(1, N+1):
    x, y = menu[i-1]
    if x == 0:
        dp[i][0] = max(dp[i-1][0]+y, dp[i-1][1]+y, dp[i-1][0])
        dp[i][1] = dp[i-1][1]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+y)

print(max(dp[N][0], dp[N][1]))
