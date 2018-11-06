class Solution(object):
  def closest(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
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
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    # write your solution here
    res = []
    while k > 0:
      cindex = self.closest(array,target)
      res.append(array[cindex])
      del(array[cindex])
      k-=1
    return res
    
