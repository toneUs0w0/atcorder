N = int(input())
A = list(map(int, input().split()))


cnts = [0] * (N+1)
ans = []
for a in A:
    cnts[a] += 1
    if cnts[a] == 2:
        ans.append(str(a))

print(" ".join(ans))
