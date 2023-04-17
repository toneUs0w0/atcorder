N = int(input())
S = input()

f = False
for s in S:
    if s == "x":
        print("No")
        exit()
    if s == "o":
        f = True
if f:
    print("Yes")
else:
    print("No")