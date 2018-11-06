

###testjj
class Queue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __len__(self):
        return len(self.__items)
#O(1)
    def enqueue(self, item):
        self.s1.append(x)

#worst case O(n)   amoritized O(1)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(s1.pop())
        return self.s2.pop()

    def is_empty(self):
        return not self.s1 and not self.s2

    def size(self):
        return len(self.s1) + len(self.s2)
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(s1.pop())
        return self.s2[-1]

  ##Time O(n)  Space O(h)
    def preorder_traversal(root):
        output = []
        if not root:
            return output
        stack = [(root, 1)]
        while stack:
            node , count = stack.pop()##pop的顺序是ABN
            if count == 1:
                output.append(node.val)
                stack.append((node , count + 1))
                if node.left:
                    stack.append((node.left, 1))
            if count == 2:##左孩子访问完了
                if node.right:
                    stack.append((node.right), 1)
        return output


####找最长连续序列 TIME O(n)   Space O(n)
    def longest(curr, parent , currlen

    def compute_area_histogram(arr):
        s = []
        area = 0
        for i in range(len(arr)+1):
            while s and (i == len(arr) or arr[i] < arr[s[len(s) - 1]]):
                height = arr[s[len(s) - 1]]
                s.pop()
                width = i

                if s:
                    width = i - s[-1] - 1
                area = max(area, height * width)
            s.append(i)
        return area
