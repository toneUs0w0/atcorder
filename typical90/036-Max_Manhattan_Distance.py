# https://atcoder.jp/contests/typical90/tasks/typical90_aj

# マンハッタン距離は45度回転

N, Q = map(int, input().split())
plots = []
for _ in range(N):
    x, y = map(int, input().split())
    plots.append((x, y))
queries = []
for _ in range(Q):
    q = int(input())
    queries.append(q)

# rotate
x_max = -1
x_min = float('Inf')
y_max = -1
y_min = float('Inf')
for x, y in plots:
    X = x - y
    Y = x + y
    x_max = max(x_max, X)
    y_max = max(y_max, Y)
    x_min = min(x_min, X)
    y_min = min(y_min, Y)

for q in queries:
    px, py = plots[q-1]
    pX = px - py
    pY = px + py
    print(max(abs(pX - x_max), abs(pX - x_min), abs(pY - y_max), abs(pY - y_min)))




