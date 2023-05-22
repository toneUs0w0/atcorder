N, M = map(int, input().split())
S = []
for _ in range(N):
    s = list(input())
    S.append(s)

#print(S)

from itertools import permutations

l = list(range(N))
P = list(permutations(l))

#print(P)

for p in P:
    #print(p)
    f = True
    for i in range(len(p)-1):
        s1 = S[p[i]]
        s2 = S[p[i + 1]]
        #print(s1, s2)
        cnt = 0
        for m in range(M):
            if s1[m] != s2[m]:
                cnt += 1
            if cnt > 1:
                f = False
                break
        if cnt != 1:
            f = False
            break
    if f:
        print("Yes")
        exit()
print("No")
    
