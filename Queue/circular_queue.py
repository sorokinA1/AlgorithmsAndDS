# class Queue:
#     def __init__(self, maxSize):
#         self.items = maxSize * [None]
#         self.maxSize = maxSize
#         self.start = -1
#         self.end = -1
#
#     def __str__(self):
#         elements = [str(x) for x in self.items]
#         return f'{elements}'
#
#     @property
#     def isFull(self):
#         if self.start == self.end + 1:
#             return True
#         elif self.start == 0 and self.end + 1 == self.maxSize:
#             return True
#         else:
#             return False
#
#     @property
#     def isEmpty(self):
#         return True if self.end == -1 else False
#
#     def enqueue(self, data):
#         if self.isFull:
#             return 'Queue is full'
#         else:
#             if self.end + 1 == self.maxSize:
#                 self.end = 0
#             else:
#                 self.end += 1
#                 if self.start == -1:
#                     self.start = 0
#             self.items[self.end] = data
#
#     def dequeue(self):
#         if self.isEmpty:
#             return '[]'
#         else:
#             firstElement = self.items[self.start]
#             start = self.start
#             if self.start == self.end:
#                 self.start = -1
#                 self.end = -1
#             elif self.start + 1 == self.maxSize:
#                 self.start = 0
#             else:
#                 self.start += 1
#                 self.items[start] = None
#             return firstElement
#
#     def peek(self):
#         return self.items[self.start]
#
#     def clear(self):
#         self.items = self.maxSize * [None]
#         self.end = -1
#         self.start = -1
#
#
# my_queue = Queue(3)
# my_queue.enqueue('Sayaka')
# my_queue.enqueue('Sakura')
# my_queue.enqueue('Ren')
# print(my_queue)
# my_queue.dequeue()
# print(my_queue)
# print(my_queue.peek())

################################################################################
################################################################################

# class Queue:
#     def __init__(self, maxSize):
#         self.max_size = maxSize
#         self.size = 0
#         self.start = 0
#         self.end = -1
#         self.items = maxSize * [None]
#
#     def __str__(self):
#         return f'{self.items}'
#
#     def enqueue(self, value):
#         if self.isFull():
#             return 'queue is full'
#         else:
#             self.end = (self.end + 1) % self.max_size
#             self.items[self.end] = value
#             self.size += 1
#
#     def dequeue(self):
#         if self.isEmpty():
#             return 'queue is empty'
#         else:
#             self.items[self.start] = None
#             self.start = (self.start + 1) % self.max_size
#             self.size -= 1
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
#             return self.items[self.end]
#         else:
#             return -1
#
#
# my_queue = Queue(3)
# print(my_queue.isFull())
# print(my_queue.isEmpty())
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# print(my_queue)
# my_queue.dequeue()
# print(my_queue)
# print(my_queue.showRear())
# print(my_queue.showFront())
# https://www.youtube.com/watch?v=2IvDFVU8Zy4

class Queue:
    def __init__(self, maxSize):
        self.max_size = maxSize
        self.size = 0
        self.start = 0
        self.end = 0  # changes here
        self.items = maxSize * [None]

    def __str__(self):
        return f'{self.items}'

    def enqueue(self, value):
        if self.isFull():
            return 'queue is full'
        else:
            self.items[self.end] = value
            self.size += 1
            self.end = (self.end + 1) % self.max_size

    def dequeue(self):
        if self.isEmpty():
            return 'queue is empty'
        else:
            self.items[self.start] = None
            self.size -= 1
            self.start = (self.start + 1) % self.max_size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def showFront(self):
        if not self.isEmpty():
            return self.items[self.start]
        else:
            return -1

    def showRear(self):
        if not self.isEmpty():
            return self.items[self.end - 1]  # changes here
        else:
            return -1


my_queue = Queue(3)
print(my_queue.isFull())
print(my_queue.isEmpty())
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue)
my_queue.dequeue()
print(my_queue)
print(my_queue.showRear())
print(my_queue.showFront())
# https://www.youtube.com/watch?v=T7sn5M1tfe0&t=339s
