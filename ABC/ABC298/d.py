from collections import deque

Q = int(input())
Qry = []
for _ in range(Q):
    q = list(map(int, input().split()))
    Qry.append(q)

P = 998244353

# あらかじめ10^m mod P を算出
n = 1
M = []
for m in range(Q+1):
    M.append(n % P)
    n = (n * 10) % P
#print(M)

num = 1
max_keta = 1
ind = deque([1])
for q in Qry:
    if q[0] == 1:
        num *= 10
        num += q[1]
        num %= P
        max_keta += 1
        ind.append(q[1])
    elif q[0] == 2:
        top_num = ind.popleft()
        dif = (top_num * M[max_keta-1]) % P
        num = (num % P - dif) % P
        max_keta -= 1
    else:
        num %= P
        print(num)




