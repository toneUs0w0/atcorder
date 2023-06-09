N, D = map(int, input().split())
m = []
for _ in range(N):
    x, y = map(int, input().split())
    m.append((x, y))

d = D**2
node = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        #print("{}-{}".format(i, j))
        x1, y1 = m[i]
        x2, y2 = m[j]
        _d = (x1 - x2)**2 + (y1 - y2)**2
        #print(_d)
        if _d > d:
            continue
        else:
            #print("add")
            node[i].append(j)
            node[j].append(i)

from collections import deque

q = deque([0])
vil = [False] * (N)
while q:
    now = q.pop()
    vil[now] = True
    for nxt in node[now]:
        if vil[nxt]:
            continue
        q.append(nxt)
        vil[nxt] = True

for tf in vil:
    if tf:
        print("Yes")
    else:
        print("No")

#print(node)


     