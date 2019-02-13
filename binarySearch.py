def binarySearch(array, target):
    if not array:
        return None
    left = 0
    right = len(array) - 1
    while left < right - 1:
        mid = (left+right)/2
      if array[mid]<target:
          left = mid
      else:
          right = mid
    if array[left] == target:
        return left
    if array[right] == target:
        return right
    return -1




 
#矩阵中找target
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Target = 10


Time complexity: O(log(N*M))
def binary_search_matrix(matrix, target):
    if matrix == None:
        return None
    N, M = len(matrix), len(matrix[0])   #N是行数, M是列数
    left, right = 0, N*M - 1
    
    while left <= right:
        mid = (left + right) / 2
        row_num = mid / M
        col_num = mid % M
        if matrix[row_num][col_num] < target:
            left = mid + 1
        elif matrix[row_num][col_num] > target:
            right = mid - 1
        else:
            return (row_num, col_num)
    return None

#找最近的数
def closest(array, target):
    if len(array)== 0 or array == None:
      return -1
    left = 0
    right = len(array)-1
    while left < right - 1:
      mid = (left+right)/2
      if array[mid]> target:
        right = mid
      elif array[mid]< target:
        left = mid
      else:
        return mid
    return left if abs(array[left]-target)<abs(array[right]-target) else right
def kClosest(array, target, k):
    res = []
    if len(array) == 0 or k == 0:
        return res
    close = cloest(array, target)
    
    res.append(array[close])
    left = close - 1
    right = close + 1
    
    while len(res) < k:
        if left >= 0 and right <= len(array) - 1:
            if abs(array[left] - target)> abs(array[right] - target):
                res.append(array[right])
                right += 1
            else:
                res.append(array[left])
                left -=1
        elif left >= 0 and right > len(array) - 1:
            res.append(array[left])
            left -=1
        elif left <0 and right <= len(array) - 1:
            res.append(array[right])
            right +=1
    return res
#这个和我最上面写的 classic binary search其实是一样的
#如果要找 last occur,  else里面放left = mid就行
def firstOccur(array, target):
    if array == None or len(array) == 0:
        return -1
    left = 0
    right = len(array) -1
    while left< right - 1:
        mid = (left + right)/2
        if array[mid] < target:
            left = mid
        else:
            right = mid
    if array[left] == target:
        return left
    if array[right] == target:
        return right

    return -1
#time O(n)
#space O(1)

rotated array
4 5 6 7 0 1 2 3
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    left = 0
    right = len(arr)-1
    while left < right - 1:
        mid = (left + right) / 2
    if arr[mid] == target:
        return mid
    if arr[left] < arr[mid]:
      if (target < arr[mid] and key >= arr[left]):
          right = mid - 1
      else:
          left = mid + 1
    elif arr[mid] < arr[right]:
      if target > arr[mid] and target <= arr[right]:
          left = mid + 1
      else:
          right = mid - 1

  if arr[st] == key:
      return st
  if arr[end] == key:
      return end
  return -1

def linear_search(a, key):
  for i in xrange(0, len(a)):
    if a[i] == key:
      return i
  return -1

def main():
  v1 = [6, 7, 1, 2, 3, 4, 5]
  print("Key(3) for Binary Search found at:" + str(binary_search_rotated(v1, 3))),
  print(", Key(3) for Linear Search found at:" + str(linear_search(v1, 3)))

  v2 = [4, 5, 6, 1, 2, 3]

  print("Key(6) for Binary Search found at:" + str(binary_search_rotated(v2, 6))),
  print(", Key(6) for Linear Search found at:" + str(linear_search(v2, 6)))

  print("Key(1) for Binary Search found at:" + str(binary_search_rotated(v2, 1))),
  print(", Key(1) for Linear Search found at:" + str(linear_search(v2, 1)))

  print("Key(5) for Binary Search found at:" + str(binary_search_rotated(v2, 5))),
  print(", Key(5) for Linear Search found at:" + str(linear_search(v2, 5)))

  print("Key(2) for Binary Search found at:" + str(binary_search_rotated(v2, 2))),
  print(", Key(2) for Linear Search found at:" + str(linear_search(v2, 2)))

  print("Key(3) for Binary Search found at:" + str(binary_search_rotated(v2, 3))),
  print(", Key(3) for Linear Search found at:" + str(linear_search(v2, 3)))

  print("Key(4) for Binary Search found at:" + str(binary_search_rotated(v2, 4))),
  print(", Key(4) for Linear Search found at:" + str(linear_search(v2, 4)))


main()
