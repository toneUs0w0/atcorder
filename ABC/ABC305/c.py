H, W = map(int, input().split())
P = []
for _ in range(H):
    p = list(input())
    P.append(p)


f_h = 100000
f_w = 100000
e_h = -1
e_w = -1

for h in range(H):
    for w in range(W):
        if P[h][w] == "#":
            f_h = min(f_h, h)
            f_w = min(f_w, w)
            e_h = max(e_h, h)
            e_w = max(e_w, w)

for h in range(f_h, e_h+1):
    for w in range(f_w, e_w+1):
        if P[h][w] == ".":
            print(h+1, w+1)
            exit()

