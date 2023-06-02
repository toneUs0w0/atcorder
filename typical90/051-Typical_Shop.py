# 半数全列挙

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

# Aを半数に分ける
B = A[:N//2]
C = A[N//2:]


def all_comb(items):
    n = len(items)
    ret = [[] for _ in range(n+1)]
    for bit in range(1 << n):
        total = 0
        cnt = 0
        for i in range(n):
            if (bit >> i) % 2 == 1:
                total += items[i]
                cnt += 1
        ret[cnt].append(total)
    for i in range(n+1):
        ret[i].sort()
    return ret

Btb = all_comb(B)
Ctb = all_comb(C)

ans = 0
for i in range(K+1): #Bからiコ選ぶ時
    j = K - i
    if i >= len(Btb) or j >= len(Ctb):
        continue
    cid = len(Ctb[j])-1
    for bid, bp in enumerate(Btb[i]):
        while cid >= 0 and bp + Ctb[j][cid] > P:
            cid -= 1
        ans += cid + 1

print(ans)






