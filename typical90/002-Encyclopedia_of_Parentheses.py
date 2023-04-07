# https://atcoder.jp/contests/typical90/tasks/typical90_b
# lv 3

# 最左で生成していくだけ
# (何個分残っているかだけ保持しておく

N = int(input())

if N % 2 != 0:
    exit()

half = N // 2

def create_brkt(amari, left, right, rtn):
    if amari == 0:
        print(rtn)
        return
    else:
        if left + 1 <= half:
            create_brkt(amari-1, left+1, right, rtn + "(")
        if right + 1 <= left and right + 1 <= half:
            create_brkt(amari-1, left, right+1, rtn + ")")

create_brkt(N, 0, 0, "")
