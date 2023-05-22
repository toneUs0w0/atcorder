N, Q = map(int, input().split())
Query = []
for _ in range(Q):
    q = list(map(int, input().split()))

cnt = [0] * (N+1)
node = [[] for _ in range(N+1)]
ans = N

for q in Query:
    if q[0] == 1:
        if cnt[q[1]] == 0:
            ans -= 1
        if cnt[q[2]] == 0:
            ans -= 1
        cnt[q[1]] += 1
        cnt[q[2]] += 1
        node[q[1]].append(q[2])
        node[q[2]].append(q[1])
        print(ans)
    else:
        for n in node[q[1]]:
            cnt[n] -= 1
            if cnt[n] == 0:
                ans += 1
        node[q[1]] = []
        ans += 1
