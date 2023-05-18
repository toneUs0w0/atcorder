N = int(input())
S = input()
fase = 0
for s in S:
    if s == "|" and fase == 0:
        fase = 1
    elif fase == 1 and s == "*":
        fase = 2
    elif fase == 2 and s == "|":
        print("in")
        exit()
print("out")
