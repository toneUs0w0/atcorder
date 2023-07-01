N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = []
for _ in range(Q):
    l, r = map(int, input().split())
    query.append((l, r))

s = 0
b = 0
total_sl = []
for i in range(len(A)):
    if i % 2 == 0:
        s += (A[i] - b)
    else:
        b = A[i]
    total_sl.append(s)
#print(total_sl)

import bisect

for l, r in query:
    ans = 0
    l_index = bisect.bisect_left(A, l)
    #print("l_index = {}".format(l_index))
    if l_index % 2 == 0: 
        ans += A[l_index] - l
        #print("ans : {}".format(ans))
    r_index = bisect.bisect_left(A, r)
    #print("r_index = {}".format(r_index))
    if r_index % 2 == 0:
        ans += r - A[r_index-1]
        #print("ans : {}".format(ans))
        r_index -= 1
    #print("{} + {} - {}".format(ans, total_sl[r_index], total_sl[l_index]))
    print(ans + total_sl[r_index] - total_sl[l_index])

    #print(l_index, r_index)




