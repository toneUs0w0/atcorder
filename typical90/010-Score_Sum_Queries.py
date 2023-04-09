# https://atcoder.jp/contests/typical90/tasks/typical90_j
# Lv 2

# 累積和配列

N = int(input())
CP = []
for _ in range(N):
    c, p = map(int, input().split())
    CP.append((c, p))
Q = int(input())
Qry = []
for _ in range(Q):
    l, r = map(int, input().split())
    Qry.append((l, r))

C1 = [0] * (N+1)
C2 = [0] * (N+1)

for i in range(1, N+1):
    c, p = CP[i-1]
    if c == 1:
        C1[i] = C1[i-1] + p
        C2[i] = C2[i-1]
    else:
        C2[i] = C2[i-1] + p
        C1[i] = C1[i-1]

for l, r in Qry:
    a = C1[r] - C1[l-1]
    b = C2[r] - C2[l-1]
    print(a, b)
    


