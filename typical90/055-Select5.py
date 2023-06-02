N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

from itertools import combinations

A = [a%P for a in A]

ans = 0

for s in range(0, N-4):
    cs = A[s]
    for t in range(s+1, N-3):
            ct = A[t]
            for u in range(t+1, N-2):
                    cu = A[u]
                    for v in range(u+1, N-1):
                            cv = A[v]
                            for w in range(v+1, N):
                                cw = A[w]
                                if cs%P*ct%P*cv%P*cu%P*cw%P == Q:
                                    ans += 1
                                        
                                


    
print(ans)