# 隣接要素のabsのみを保持更新する

N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = []
for _ in range(Q):
    l, r, v = map(int, input().split())
    query.append((l-1, r-1, v))

dif = [[0, 0] for _ in range(N)]

ans = 0
for i in range(N-1):
    dif[i][0] = A[i]
    dif[i][1] = A[i+1]
    ans += abs(A[i] - A[i+1])

#print(dif)
#print(ans)

for l, r, v in query:
    if l > 0:
        ans -= abs(dif[l-1][0] - dif[l-1][1])
        dif[l-1][1] += v
        ans += abs(dif[l-1][0] - dif[l-1][1])
        #print(dif)
    if r < N-1:
        ans -= abs(dif[r][0] - dif[r][1])
        dif[r][0] += v
        ans += abs(dif[r][0] - dif[r][1])
    print(ans)
    #print(dif)



