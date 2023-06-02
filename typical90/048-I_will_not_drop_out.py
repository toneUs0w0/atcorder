# 部分点リストと完答リストを管理

N, K = map(int, input().split())
AB = []
for _ in range(N):
    AB.append(tuple(map(int, input().split())))

AB = sorted(AB, key=lambda x:-x[1])

import heapq
kantou = []
heapq.heapify(kantou)

ans = 0
ab_id = 0
for k in range(K):
    if ab_id >= N:
        if len(kantou) <= 0:
            break
        else:
            a, b = -1, -1
    else:
        a, b = AB[ab_id]

    ka = 0
    if len(kantou) > 0:
        ka = -heapq.heappop(kantou)
        
    if b > ka:
        ans += b
        ab_id += 1
        heapq.heappush(kantou, -ka)
        heapq.heappush(kantou, -(a-b))
    else:
        ans += ka

print(ans)






