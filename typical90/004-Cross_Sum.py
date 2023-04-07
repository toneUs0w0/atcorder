# https://atcoder.jp/contests/typical90/tasks/typical90_d
# Lv. 2

# 累積和

H, W = map(int, input().split())
A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

H_sum = [0] * H
W_sum = [0] * W
for h in range(H):
    for w in range(W):
        H_sum[h] += A[h][w]
        W_sum[w] += A[h][w]

rtn = ""
for h in range(H):
    for w in range(W):
        rtn += str(H_sum[h] + W_sum[w] - A[h][w]) + " "
    rtn += "\n"

print(rtn[:-1])