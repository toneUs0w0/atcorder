# 最長増加部分列

N = int(input())

A = list(map(int, input().split()))

# 前方向のLIS

import bisect

fwd_lis = [float('Inf')] * (N+1)
fwd_mems = []
for a in A:
    index = bisect.bisect_left(fwd_lis, a)
    fwd_mems.append(index)
    fwd_lis[index] = a

bck_lis = [float('Inf')] * (N+1)
bck_mems = [0] * N
for i in range(1, len(A)+1):
    a = A[len(A) - i]
    index = bisect.bisect_left(bck_lis, a)
    bck_mems[len(A) - i] = index
    bck_lis[index] = a

ans = 0
for k in range(N):
    ans = max(ans, fwd_mems[k] + bck_mems[k] + 1)

print(fwd_mems)
print(bck_mems)
print(ans)

