# 表示は５桁なのでボタンを10^5回押すまでの何処かで必ずループに入る

N, K = map(int, input().split())

apear_order = [-1] * (100000)

k = 0
apear_order[N] = K
before_n = N

for _ in range(10000):
    k += 1
    tmp = before_n
    for i in [10000, 1000, 100, 10, 1]:
        _st = tmp // i
        before_n += _st
        tmp -= i * _st
    before_n %= 100000
    if apear_order[before_n] != -1:
        print("roop start:{} end:{}".format(apear_order[before_n], k))
        break


