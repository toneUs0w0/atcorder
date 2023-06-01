# https://atcoder.jp/contests/typical90/tasks/typical90_ar
# Aのシフト状態を管理する

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = []
for _ in range(Q):
    q = list(map(int, input().split()))
    Query.append(q)

shift = 0

for q in Query:
    t1, t2, t3 = q[0], q[1]-1, q[2]-1
    if t1 == 2:
        shift += 1
        shift %= N
    elif t1 == 1:
        t2 = (N + t2 - shift) % N
        t3 = (N + t3 - shift) % N
        #print("change index {} and {}".format(t2, t3))
        tmp = A[t2]
        A[t2] = A[t3]
        A[t3] = tmp
    else:
        t2 = (N + t2 - shift) % N
        print(A[t2])
    #print(A)