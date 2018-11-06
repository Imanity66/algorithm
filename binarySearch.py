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
