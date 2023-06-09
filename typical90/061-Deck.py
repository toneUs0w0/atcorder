Q = int(input())
query = []
for _ in range(Q):
    t, x = map(int, input().split())
    query.append((t, x))

d_top = []
d_bottom = []


for t, x in query:
    if t == 1:
        d_top.append(x)
    elif t == 2:
        d_bottom.append(x)
    else:
        if x <= len(d_top):  # bottomから取る
            print(d_top[len(d_top) - x])
        else:
            print(d_bottom[x - len(d_top) - 1])


