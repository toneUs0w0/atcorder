N = int(input())
s = 0
t = N - 1
while(1):
    mid = (s + t) // 2
    print ("? {}".format(mid + 1))
    out = int(input())
    if out == 0:
        s = mid
    else:
        t = mid
    if abs(s-t) <= 1:
        print("! {}".format(s + 1))
        exit()
    