N = int(input())
LR = []
for _ in range(N):
    l, r = map(int, input().split())
    LR.append((l, r))

ans = 0
for i in range(N-1):
    l1, r1 = LR[i]
    for j in range(i+1, N):
        l2, r2 = LR[j]
        t = 0
        s = (r1 - l1 + 1) * (r2 - l2 + 1)
        #print("[{}-{}] - [{}-{}]".format(l1, r1, l2, r2))
        if s == 0:
            continue
        for k in range(l1, r1+1):
            #print("k = {}".format(k))
            if k <= l2:
                #print("k <= r2")
                continue
            elif k > r2:
                t += (r2 - l2 + 1)
            else:
                #print("t += {}".format(max(0, r2-k)))
                t += max(0, k-l2)
        ans += t / s
print(ans)


