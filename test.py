# def isEven(n):
#     if n | 1 > n:
#         return True
#     else:
#         return False


def isEven(value):
    return value | 1 > value


print(isEven(3))


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    # create class with predefined node
    def __init__(self, space):
        self.space = space  # capacity
        self.start = Node()
        self.end = Node(prev=self.start)
        self.start.next = self.end

    def __str__(self):
        # helper method for showing nodes
        elements = []
        cur_node = self.start.next
        while cur_node.next:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return f'{elements}'

    def __len__(self):
        count = 0
        cur_node = self.start.next
        while cur_node.next:
            cur_node = cur_node.next
            count += 1
        return count

    def enqueue(self, value):
        if self.isFull:
            return 'Queue is full'
        else:
            new_node = Node(value, next=self.end, prev=self.end.prev)
            self.end.prev.next = new_node
            self.end.prev = new_node
            self.space -= 1

    def dequeue(self):
        if self.isEmpty:
            return '[]'
        else:
            self.start.next = self.start.next.next
            self.start.next.prev = self.start
            self.space += 1

    @property
    def isEmpty(self):
        return self.start.next == self.end

    @property
    def isFull(self):
        return self.space == 0

    def showFront(self):
        if not self.isEmpty:
            return self.start.next.data
        else:
            return -1

    def showRear(self):
        if not self.isEmpty:
            return self.end.prev.data
        else:
            return -1


# Bitwise операции гораздо быстрее чем арифметические, потому что работают напрямую с битами. Минус: сложность восприятия и неочевидность решения.
#
# def isEven(value):
#     return value | 1 > value


# Реализовать буфер можно с помощью связного списка или массива. Очередь может быть с ограничением размера или нет. Я приведу примеры с ограниченным размером.
#
# 1.  Лучшей реализацией будет использование связного списка, потому что time and space complexity на все операции будет O(1). Я вижу только один ее минус - нужно писать много кода. Я не уверен к этому способу нужны комментарии - я разбил реализацию на много маленьких методов, название которых уже объясняет, что они делают:
#
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
# class Queue:
#     # create class with predefined node
#     def __init__(self, space):
#         self.space = space
#         self.start = Node()
#         self.end = Node(prev=self.start)
#         self.start.next = self.end
#
#     def __str__(self):
#         # helper method for showing nodes
#         elements = []
#         cur_node = self.start.next
#         while cur_node.next:
#             elements.append(cur_node.data)
#             cur_node = cur_node.next
#         return f'{elements}'
#
#     def __len__(self):
#         # show length
#         count = 0
#         cur_node = self.start.next
#         while cur_node.next:
#             cur_node = cur_node.next
#             count += 1
#         return count
#
#     def enqueue(self, value):
#         if self.isFull:
#             return 'Queue is full'
#         else:
#             new_node = Node(value, next=self.end, prev=self.end.prev)
#             self.end.prev.next = new_node
#             self.end.prev = new_node
#             self.space -= 1
#
#     def dequeue(self):
#         if self.isEmpty:
#             return '[]'
#         else:
#             self.start.next = self.start.next.next
#             self.start.next.prev = self.start
#             self.space += 1
#
#     @property
#     def isEmpty(self):
#         return self.start.next == self.end
#
#     @property
#     def isFull(self):
#         return self.space == 0
#
#     def showFront(self):
#         if not self.isEmpty:
#             return self.start.next.data
#         else:
#             return -1
#
#     def showRear(self):
#         if not self.isEmpty:
#             return self.end.prev.data
#         else:
#             return -1
#
# 2.
# class Queue:
#     # create queue with predefined size of maxSize
#     def __init__(self, maxSize):
#         self.max_size = maxSize
#         self.size = 0
#         self.start = 0
#         self.end = 0
#         self.items = maxSize * [None]
#
#     def __str__(self):
#         return f'{self.items}'
#
#     def enqueue(self, value):
#         if self.isFull():
#             return 'queue is full'
#         else:
#             self.items[self.end] = value
#             self.size += 1
#             self.end = (self.end + 1) % self.max_size
#
#     def dequeue(self):
#         if self.isEmpty():
#             return 'queue is empty'
#         else:
#             self.items[self.start] = None
#             self.size -= 1
#             self.start = (self.start + 1) % self.max_size
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def isFull(self):
#         return self.size == self.max_size
#
#     def showFront(self):
#         if not self.isEmpty():
#             return self.items[self.start]
#         else:
#             return -1
#
#     def showRear(self):
#         if not self.isEmpty():
#             return self.items[self.end - 1]
#         else:
#             return -1


arr = [1, 2, 3, 4]




