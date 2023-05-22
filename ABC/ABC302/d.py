N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
A.reverse()
B.sort()
B.reverse()

sa = 0
sb = 0
ans = 0
while 1:
    if sa >= len(A) or sb >= len(B):
        ans = -1
        break
    if abs(A[sa] - B[sb]) <= D:
        ans = A[sa] + B[sb]
        break
    if sa == len(A) - 1 or A[sa] < B[sb]:
        sb += 1
    else:
        sa += 1

print(ans)
