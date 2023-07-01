# 不便さ最小の発電所の(x, y)は工場のいずれかの(X, Y)と一致する
N = int(input())
plots = []
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    plots.append((x, y))
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
#print("X")
minx = X[0]
sum_abs_x = 0
for i in range(1, N):
    x = X[i]
    sum_abs_x += abs(x - minx)
min_sum_abs_x = sum_abs_x
before_x = X[0]
cand_sum = sum_abs_x
for i in range(1, N):
    #print(cand_sum)
    x = X[i]
    dx = x - before_x
    cand_sum += i * dx
    cand_sum -= (N-i)*dx
    if cand_sum < min_sum_abs_x:
        min_sum_abs_x = cand_sum
    before_x = x

#print("Y")
miny = Y[0]
sum_abs_y = 0
for i in range(1, N):
    y = Y[i]
    sum_abs_y += abs(y - miny)
min_sum_abs_y = sum_abs_y
before_y = Y[0]
cand_sum = sum_abs_y
for i in range(1, N):
    #print(cand_sum)
    y = Y[i]
    dy = y - before_y
    cand_sum += i * dy
    cand_sum -= (N-i)*dy
    if cand_sum < min_sum_abs_y:
        min_sum_abs_y = cand_sum
    before_y = y

print(min_sum_abs_x+min_sum_abs_y)






