N = int(input())
A = list(map(int, input().split()))
S = list(input())
d = {"M":0, "E":1, "X":2}

#m0, m1, m2, 0 - 2
# m0e0, m0e1, ... 3 - 11
# m0e0x0, m0e0x1, m0e1x0, m0e1x1, ... 12 - 39
nam1 = ["", "0", "1", "2"]
nam2 = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
nam3 = []
for na in nam2:
    for n in ["0", "1", "2"]:
        nam3.append(na + n)

nam = nam1 + nam2 + nam3
dn = {}
for na in nam:
    dn[na] = 0

#print(dn)

dp = [dn for _ in range(N+1)]

for i in range(N):
    a = A[i]
    s = d[S[i]]
    for n in nam1:
        dp[i+1][n] = dp[i][n]
    if s == 0:
        dp[i+1][str(a)] += 1
    for l in [0, 1, 2]:
        for k in [0, 1, 2]:
            dp[i+1][str(l)+str(k)] = dp[i][str(l)+str(k)]
    if s == 1:
        for l in [0, 1, 2]:
            dp[i+1][str(l)+str(a)] += dp[i][str(l)]
    for l in [0, 1, 2]:
        for k in [0, 1, 2]:
            for p in [0, 1, 2]:
                dp[i+1][str(l)+str(k)+str(p)] = dp[i][str(l)+str(k)+str(p)]
    if s == 2:
        for l in [0, 1, 2]:
            for k in [0, 1, 2]:
                dp[i+1][str(l)+str(k)+str(a)] += dp[i+1][str(l)+str(k)]

#print(dp)

ans = 0

for k in [0, 1, 2]:
    for l in [0, 1, 2]:
        for m in [0, 1, 2]:
            if 0 not in [k, l, m]:
                c = 0
            elif 1 not in [k, l, m]:
                c = 1
            elif 2 not in [k, l, m]:
                c = 2
            else:
                c = 3

            #print("{} {} {}".format(str(k)+str(l)+str(m), dp[N][str(k)+str(l)+str(m)], c))
            ans += dp[N][str(k)+str(l)+str(m)] * c
print(ans)




