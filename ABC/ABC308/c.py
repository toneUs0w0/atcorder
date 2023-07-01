N = int(input())
L = []
for i in range(N):
    a, b = map(int, input().split())
    L.append((a, b, i))

def merge_sort(data):             
  if len(data) <= 1:                 #[2]
     return data                     #[2]
  mid = len(data)//2                 #[3]
  left = merge_sort(data[:mid])      #[4]
  right = merge_sort(data[mid:])     #[4]
  return merge(left,right)           #[5]

def merge(left,right):
  result = []
  i,j = 0,0
  while (i < len(left)) and (j < len(right)): #left,rightのリストの要素数よりもi,jがそれぞれ小さい場合
    if left[i] <= right[j]:                   #[6]i番目のleftの要素よりもj番目のrightの要素が大きい場合
      result.append(left[i])                  #left[i]をresultに追加
      i += 1
    else:                                     #i番目のleftの要素がj番目のrightの要素よりも大きい場合
      result.append(right[j])                 #right[j]をresultに追加
      j += 1
  if i < len(left):                           #iがleftの要素数よりも小さければ
    result.extend(left[i:])                   #i番目よりも後をresultに結合
  if j < len(right):                          #iがrightの要素数よりも小さければ
    result.extend(right[j:])                  #j番目よりも後をresultに結合
  return result
print(merge_sort(data))


