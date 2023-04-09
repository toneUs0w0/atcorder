# https://atcoder.jp/contests/typical90/tasks/typical90_f
# Lv. 5

# 文字列のn番目以降で最も左に登場する[a-z]のindexを用意しておく
# 出力する次の文字は, 残りの文字数が足りる中で最も若い[a-z]となる

N, K = map(int, input().split())
S = input()

alf_index = [[] for _ in range(26)]
for n in range(N):
    s_int = ord(S[n]) - 97
    alf_index[s_int].append(n)

for m in range(26):
    alf_index[m].append(float("Inf"))

#print(alf_index)

index_map = [[float("Inf")] * N for _ in range(26)]
for alf_int in range(26):
    i = 0
    next = alf_index[alf_int][i]
    for n in range(N):
        if n <= next:
            index_map[alf_int][n] = next
        else:
            i += 1
            next = alf_index[alf_int][i]
            index_map[alf_int][n] = next

#print(index_map)

ank = 0
ans = ""
for k in range(K):
    remain = K - k
    #print("{}th char - {} remain".format(k, remain))
    for n in range(26):
        #print("{}[{}] = {}".format(chr(n + 97), ank, index_map[n][ank]))
        if N - index_map[n][ank] >= remain:
            ans += chr(n + 97)
            #print(ans)
            ank = index_map[n][ank] + 1
            break

print(ans)