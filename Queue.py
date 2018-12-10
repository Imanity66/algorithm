
#O(n) for dequeue 其余都是O(1)
class Queue(object):
    def __init__(self):
        self.__items = []

    def __len__(self):
        return len(self.__items)
    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if self.empty():
            return None

        item = self.__items[0]
        del self.__items[0]
        return item

    def empty(self):
        return len(self.__items) == 0
    def front(self):
        if self.empty():
            return None
        return self.__items[0]


用O(1)时间得到最小值
from collections import deque
class Queue(object):
    def __init__(self):
        self.deque = deque()#deque用来存所有数据
        self.mins = deque()#存可能的最小值
    def __len__(self):
        return len(self.deque)
    def empty(self):
        return len(self.deque) == 0
    def enqueue(self, value):
        self.deque.append(value)
        while self.mins and self.mins[-1] > value :
            self.mins.pop()
        self.append(value)
    def dequeue(self):
        value = self.deque.popleft()
        if value == self.mins[0]:
            self.mins.popleft()
        return value
    def front(self):
        return self.deque[0]
    def minvalue(self):
        retirm self.mins[0]



class Stack(object):
    def __init__(self):
        self.__items = []

    def __len__(self):
    return len(self.__items)
    def empty(self):
        return len(self.__items) == 0
    def push(self, item):
        self.__items.append(item)
    def pop(self):
        if self.empty():
            return None
        return self.__items.pop()

    def top(self):
        if self.empty():
            return None
        return self.__items[-1]






Given a string containing just the characters
 '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 The brackets must close in the correct order.


 def is_valid(brackets):
     left_bracket = []
     matching_bracket = {'(':')', '{':'}', '[': ']'}
     for b in brackets:
         if b in matching_bracket:
             left_bracket.append(b)
         elif not left_bracket or matching_bracket[left_bracket[-1]] != b:
             return False
         else:
             left_bracket.pop()
     return not left_bracket
 #not + null 返回 True

  def score(brackets):
      left = 0
      res = 0
      for x in brackets:
          if x == "(":
              left += 1
          elif left != 0 and x ==")":
              res += 2 ** (left - 1)
              left = 0
      return res

#用stack做
def score(s):
    r = [0]
    for p in s:
        if p =='(':
            r.append(0)
        else:
            last = r.pop()
            if last == 0:#第一次看到右括号 last就是0 ,第一次右括号得1 其他时候乘2
                last = 1
            else:
                last *= 2
            r[-1] += last
    return r[0]
