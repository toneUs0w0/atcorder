# 行の選び方は高々 2**8 = 256 より、各選び方において部分グリッド最大となる列を選べば良い
# 事前に各列の(数, 配置)を把握しておく [* * * 4 * 4 4 *] -> (4, b00010110) += 1

H, W = map(int, input().split())
p = []
for _ in range(H):
    p.append(list(map(int, input().split())))

num_pos = [[0]*(1<<H) for _ in range(H*W+1)]

for w in range(W):
    d = {}
    for h in range(H):
        if p[h][w] not in d:
            d[p[h][w]] = 1<<h
        else:
            d[p[h][w]] += 1<<h
    #print(d)
    for num in d:
        for i in range(1, 1<<H):
            if d[num] & i == i:
                num_pos[num][i] += 1

#print(num_pos)

bt = []
for i in range(1<<H):
    j = 0
    while i > 0:
        if i & 1 > 0:
            j += 1
        i = i>>1
    bt.append(j)
#print(bt)

ans = 0
for a in range(H*W+1):
    for i in range(1<<H):
        ans = max(ans, num_pos[a][i] * bt[i])

print(ans)


