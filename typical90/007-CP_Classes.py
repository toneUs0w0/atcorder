# https://atcoder.jp/contests/typical90/tasks/typical90_g
# Lv 3

# クラスと生徒のレーティングを同じ配列内でソート
# ある生徒にとって最も不満度の小さいクラスは, ソートした際に近かった前後２レートのどちらか
# 前からと後ろから最も近いクラスとの絶対値を計算

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
for _ in range(Q):
    b = int(input())
    B.append(b)

AB = []

for a in A:
    AB.append((a, -1))
for bn in range(len(B)):
    b = B[bn]
    AB.append((b, bn))

AB.sort()

anses = [float("Inf")] * (len(B))
before = -float("Inf")
for ab, l in AB:
    if l == -1:
        before = ab
    else:
        anses[l] = min(anses[l], abs(ab - before))

AB.reverse()
after = float("Inf")
for ab, l in AB:
    if l == -1:
        after = ab
    else:
        anses[l] = min(anses[l], abs(ab - after))

for ans in anses:
    print(ans)




