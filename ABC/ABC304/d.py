# 次元圧縮
# 二次元累積和?

W, H = map(int, input().split())
N = int(input())
berry = []
xl = []
yl = []
for n in range(N):
    p, q = map(int, input().split())
    berry.append((p, q, n))
    xl.append((p, n+1))
    yl.append((q, n+1))

A_num = int(input())
A = list(map(int, input().split()))
B_num = int(input())
B = list(map(int, input().split()))

'''
for a in A:
    xl.append(a)
for b in B:
    yl.append(b)

Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(xl))))}
Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(yl))))}

for p, q in berry:
    print(Xdict[p], Ydict[q])

print([Xdict[x] for x in A])
print([Ydict[y] for y in B])
'''

for b in B:
    yl.append((b, 0))
yl = sorted(yl, key=lambda x:x[1])
yl = sorted(yl, key=lambda x:x[0])

y_by2boxid = [-1] * (N+1)
box_id = 0
for y, i in yl:
    if i == 0:
        box_id += 1
    else:
        y_by2boxid[i] = box_id

for a in A:
    xl.append((a, 0))
xl = sorted(xl, key=lambda x:x[1])
xl = sorted(xl, key=lambda x:x[0])
#print(xl)

x_by2boxid =[-1] * (N+1)
box_id = 0
for x, i in xl:
    if i == 0:
        box_id += 1
    else:
        x_by2boxid[i] = box_id

#print(x_by2boxid)
#print(y_by2boxid)

cake = {}
for n in range(1, N+1):
    xp = x_by2boxid[n]
    yp = y_by2boxid[n]
    if xp*(N+1) + yp not in cake:
        cake[xp*(N+1) + yp] = 1
    else:
        cake[xp*(N+1) + yp] += 1

min_ans = 0
if len(cake) == (A_num+1) * (B_num+1):
    min_ans = min(cake.values())
print(min_ans, max(cake.values()))
#print(cake)




    

