H, W = map(int, input().split())
S = []
for _ in range(H):
    s = list(input())
    S.append(s)

from collections import deque

q = deque([(0, 0, 0)])
check = [[False] * W for _ in range(H)]
d = {"s":0, "n":1, "u":2, "k":3, "e":4}
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    #print(q)
    nx, ny, c = q.pop()
    if nx == H-1 and ny == W-1:
        print("Yes")
        exit()
    check[nx][ny] = True
    for dx, dy in dxy:
        #print(dx+nx, dy+ny)
        if nx + dx < 0 or nx + dx >= H or ny + dy < 0 or ny + dy >= W or check[nx+dx][ny+dy] or S[nx+dx][ny+dy] not in d:
            #print("out")
            continue
        #print("{} {}".format(d[S[nx+dx][ny+dy]], (c+1)%5))
        if d[S[nx+dx][ny+dy]] == (c+1)%5:
            
            q.append((nx+dx, ny+dy, (c+1)%5))
            check[nx+dx][ny+dy] = True

print("No")






