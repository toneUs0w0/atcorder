# https://atcoder.jp/contests/typical90/tasks/typical90_a

# 最小値の最大化 -> 二分探索
# スコアS以上の分割が可能かを判定, スコアは 1 <= S <= 10^9 なので O(logL)
# あとは左から切り分けていけば良い O(K)

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# スコアの達成が可能かどうかを判定
def judge_s(s):
    cut = 0
    a0 = 0
    for a in A:
        l = a - a0
        if l >= s:
            cut += 1
            #print("{}s cut l = {}".format(cut, l))
            a0 = a
            if cut == K:
                break
    amari = L - a0
    if amari < s or cut != K:
        #print("judge({}) = false".format(s))
        return False
    else:
        #print("judge({}) = true".format(s))
        return True

def bi_search():
    st = 0
    ed = L
    while abs(ed - st) > 1:
        mid = (st + ed) // 2
        #print("bi search {} - {} mid : {}".format(st, ed, mid))
        if judge_s(mid):
            st = mid
        else:
            ed = mid
    if judge_s(st):
        return st
    elif judge_s(ed):
        return ed
    else:
        return -1

rtn = bi_search()
print(rtn)
