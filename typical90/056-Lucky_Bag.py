# 普通にやると2^100
# 普通にdp
N, S = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

dp = [[False]*(S+1) for _ in range(N+1)]
cose = [[""]*(S+1) for _ in range(N+1)]
dp[0][0] = True

for n in range(1, N+1):
    #print(cose)
    #print(dp)
    a, b = AB[n-1]
    for s in range(S+1):
        if dp[n-1][s] == False:
            #print("dp[{}][{}] is False".format(n-1, s))
            continue
        if a + s <= S:
            #print("cose[{}][{}] = {}".format(n, a+s, cose[n-1][s] + "A") )
            cose[n][a+s] = cose[n-1][s] + "A"
            dp[n][a+s] = True
        if b + s <= S:
            #print("cose[{}][{}] = {}".format(n, b+s, cose[n-1][s] + "B") )
            cose[n][b+s] = cose[n-1][s] + "B"
            dp[n][b+s] = True

if dp[N][S] == False:
    print("Impossible")
else:
    print(cose[N][S])