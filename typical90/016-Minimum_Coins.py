# https://atcoder.jp/contests/typical90/tasks/typical90_p
# lv 3

# ax + by = N を目指すナップサック問題
# aとbを[0:10000]で探すとTLEなので, a決定後はユークリッドで持っていく持っていく必要がある？
# そんなことなかった
N = int(input())
A, B, C = map(int, input().split())
tmp = [A, B, C]
tmp.sort()
A, B, C = tmp[2], tmp[1], tmp[0]
ans = float("Inf")

for an in range(10000):
    if N - (A * an) < 0:
        break
    #print("an :{}".format(an))
    for bn in range(10000 - an):
        #print("bn :{}".format(bn))
        rem = N - (A * an) - (B * bn)
        if rem < 0:
            break
        #print("rem :{}".format(rem) )
        if rem % C == 0:
            ans = min(ans, rem//C + an + bn)

print(ans)