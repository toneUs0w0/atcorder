N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

dic = {}
for i in range(M):
    dic[D[i]] = P[i+1]

cnt = 0
for c in C:
    if c in dic:
        cnt += dic[c]
    else:
        cnt += P[0]

print(cnt)


