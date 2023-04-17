# https://atcoder.jp/contests/typical90/tasks/typical90_ab
# lv 4

# 初見クリアできず
# 二次元いもす法

N = int(input())
M = 1001
cel = [[0] * (M + 1) for _ in range(M + 1)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    cel[lx][ly] += 1
    cel[rx][ly] -= 1
    cel[lx][ry] -= 1
    cel[rx][ry] += 1

#print(cel)

# x方向の加算
cel2 = [[0] * (M + 1) for _ in range(M + 1)]
for y in range(M + 1):
    cel2[0][y] = cel[0][y]
    for x in range(1, M + 1):
        cel2[x][y] = cel2[x-1][y] + cel[x][y]

#print(cel2)

# y 方向の加算
cel3 = [[0] * (M + 1) for _ in range(M + 1)]
for x in range(M + 1):
    cel3[x][0] = cel2[x][0]
    for y in range(M + 1):
        cel3[x][y] = cel3[x][y-1] + cel2[x][y]

#print(cel3)

k = [0] * (N + 1)
for x in range(M + 1):
    for y in range(M + 1):
        k[cel3[x][y]] += 1

for n in range(1, N + 1):
    print(k[n])



