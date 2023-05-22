# https://atcoder.jp/contests/typical90/tasks/typical90_ah

# 尺取法
# logNで重複を検索, logNで値の削除ができればok

N, K = map(int, input().split())
A = list(map(int, input().split()))

nums = {A[0]:1}
kinds = 1
length = 1
head = 0
tail = 0
ans = 0

while 1:
    #print(nums)
    if head > N-2:
        break
    
    if kinds < K:
        if A[head + 1] not in nums:
            nums[A[head + 1]] = 1
            kinds += 1
        else:
            if nums[A[head + 1]] == 0:
                kinds += 1
            nums[A[head + 1]] += 1
        length += 1
        ans = max(ans, length)
        head += 1
        continue

    if kinds == K:
        if A[head + 1] in nums:
            if nums[A[head + 1]] > 0:
                nums[A[head + 1]] += 1
                length += 1
                ans = max(ans, length)
                head += 1
                continue

    nums[A[tail]] -= 1
    if nums[A[tail]] == 0:
        kinds -= 1
    tail += 1
    length -= 1


print(ans)









