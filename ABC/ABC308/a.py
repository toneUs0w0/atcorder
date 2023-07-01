S = list(map(int, input().split()))
before = -1
for s in S:
    if before > s or s % 25 != 0 or 100 > s or 675 < s:
        print("No")
        exit()
    before = s
print("Yes")
