H, W = map(int, input().split())
S = []
for _ in range(H):
    s = list(input())
    S.append(s)

dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
l = ["n", "u", "k", "e"]
ans = []


for h in range(H):
    for w in range(W):
        if S[h][w] == "s":
            for dx, dy in dxdy:
                sh = h
                sw = w
                k = 0
                for i in range(5):
                    if sh + dx < 0 or sh + dx >= H or sw + dy < 0 or sw + dy >= W:
                        break
                    sh += dx
                    sw += dy
                    if S[sh][sw] != l[k]:
                        break
                    if k == 3:
                        ans = [h, w, dx, dy]
                        break
                    k += 1

x, y = ans[0]+1, ans[1]+1
print(x, y)
for i in range(4):
    x += ans[2]
    y += ans[3]
    print(x, y)