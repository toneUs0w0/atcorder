N = int(input())
Q = int(input())
Qry = []
for _ in range(Q):
    qry = list(map(int, input().split()))
    Qry.append(qry)

#import heapq
N = 200000
box = [[] for _ in range(N + 1)]
card = [[] for _ in range(N + 1)]
w = []
#heapq.heapify(w)
for q in Qry:
    if q[0] == 1:
        box[q[2]].append(q[1])
        card[q[1]].append(q[2])
    elif q[0] == 2:
        box[q[1]].sort() 
        print(" ".join([str(x) for x in box[q[1]]]))
    else:
        card[q[1]].sort() 
        print(" ".join([str(x) for x in set(card[q[1]])]))
#print(box)
