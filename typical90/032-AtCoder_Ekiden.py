# https://atcoder.jp/contests/typical90/tasks/typical90_af
# 順列列挙


N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
M = int(input())
sim = [[False]*11 for _ in range(11)]
for _ in range(M):
    x, y = map(int, input().split())
    sim[x][y] = True
    sim[y][x] = True

#print(A)
import itertools
per = list(itertools.permutations(range(1,N+1))) #順列生成
ans = 100000
for p in per:
    #print(p)
    f = False
    score = 0
    for i in range(len(p)-1):
        if sim[p[i]][p[i+1]] or sim[p[i+1]][p[i]]:
            f = True
            break
        score += A[p[i]-1][i]
    if f:
        continue
    score += A[p[len(p)-1]-1][len(p)-1]
    ans = min(ans, score)
    #print(score)

if ans == 100000:
    print(-1)
else:
    print(ans)

