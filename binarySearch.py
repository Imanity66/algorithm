class Solution(object):
  def binarySearch(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if array==None or len(array)==0:
      return -1
    left = 0
    right = len(array) - 1
    while left <= right :
      mid = (left+right)/2
      if array[mid]>target:
        right = mid - 1
      elif array[mid]<target:
        left = mid +1
      else:
        return mid
    return -1




rotated array
def binary_search(arr, key):
  #TODO: Write - Your - Code
  st = 0
  end = len(arr)-1
  if st > end:
    return -1
  while st < end - 1:
    mid = (st + end)/2

    if arr[mid] == key:
      return mid

    if (arr[st] < arr[mid]):
      if (key < arr[mid] and key >= arr[st]):
        end = mid - 1
      else:
        st = mid + 1
    elif (arr[mid] < arr[end]):
      if(key > arr[mid] and key <= arr[end]):
        st = mid + 1
      else:
        end = mid - 1

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
