# 0mod46の組み合わせを考える
# https://atcoder.jp/contests/typical90/submissions/me

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

baket_a = [0] * 46
for a in A:
    baket_a[a%46] += 1

baket_b = [0] * 46
for b in B:
    baket_b[b%46] += 1

baket_c = [0] * 46
for c in C:
    baket_c[c%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46 != 0:
                continue
            ans += baket_a[i] * baket_b[j] * baket_c[k]

print(ans)


