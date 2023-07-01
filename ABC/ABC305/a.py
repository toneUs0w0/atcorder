N = int(input())
t = 0
ans_t = 0
ans = 100000
for n in range(21):
    if ans > abs(t-N):
        ans = abs(t-N)
        ans_t = t
    t += 5

print(ans_t)
