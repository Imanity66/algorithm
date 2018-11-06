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
