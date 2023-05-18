N = int(input())
S = input()

cnts = []
cnt = 0
for s in S:
    if s == "-":
        if cnt != 0:
            cnts.append(cnt)
        cnts.append(-1)
        cnt = 0
    if s == "o":
        cnt += 1
if cnt != 0:
    cnts.append(cnt)



ans = -1
for i in range(1, len(cnts)):
    s = cnts[i-1]
    t = cnts[i]
    if (s > 0 and t < 0) or (s < 0 and t > 0):
        ans = max(max(s, t), ans)

print(ans)

