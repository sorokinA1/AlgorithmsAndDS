# Single Linked List:

# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# class CircularLinkedList:
#     def __init__(self, head=None, end=None):
#         self.head = head
#         self.end = end
#
#     def display(self):
#         if self.head is None:
#             print('[]')
#         else:
#             elements = []
#             cur_node = self.head
#             while cur_node:
#                 elements.append(cur_node.data)
#                 cur_node = cur_node.next
#                 if cur_node == self.head:
#                     break
#             print(elements)
#
#     @property
#     def length(self):
#         total = 0
#         cur_node = self.head
#         while cur_node:
#             cur_node = cur_node.next
#             total += 1
#             if cur_node == self.head:
#                 break
#         return total
#
#     def push(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.head.next = new_node
#             self.end = new_node
#         else:
#             self.end.next = new_node
#             new_node.next = self.head
#             self.end = new_node
#
#     def unshift(self, data):
#         if self.head is None:
#             self.push(data)
#         else:
#             new_node = Node(data, self.head)
#             self.head = new_node
#             self.end.next = new_node
#
#     def insert(self, index, data):
#         if index < 0 or index > self.length:
#             raise IndexError('oops')
#         elif index == 0:
#             self.unshift(data)
#         elif index == self.length:
#             self.push(data)
#         else:
#             count = 0
#             cur_node = self.head
#             while count < index - 1:
#                 cur_node = cur_node.next
#                 count += 1
#             cur_node.next = Node(data, cur_node.next)
#
#     def delete_beg(self):
#         if self.head is None:
#             raise ValueError
#         else:
#             self.end.next = self.head.next
#             self.head = self.head.next
#
#     def delete_end(self):
#         if self.head is None:
#             raise ValueError('oops')
#         else:
#             cur_node = self.head
#             while cur_node.next.next != self.head:
#                 cur_node = cur_node.next
#             self.end = cur_node
#             cur_node.next = self.head
#
#     def delete_mid(self, index):
#         if index < 0 or index > self.length:
#             raise IndexError('oops')
#         if index == 0:
#             self.delete_beg()
#         if index == self.length:
#             self.delete_end()
#         else:
#             count = 0
#             cur_node = self.head
#             while count < index - 1:
#                 cur_node = cur_node.next
#                 count += 1
#             cur_node.next = cur_node.next.next

########################################################

# Double Linked List
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# class Linked_list:
#     def __init__(self, head=None):
#         self.head = head
#
#     def display(self):
#         if self.head is None:
#             print('[]')
#         else:
#             elements = []
#             cur_node = self.head
#             while cur_node:
#                 elements.append(cur_node.data)
#                 cur_node = cur_node.next
#             print(elements)
#
#     @property
#     def length(self):
#         total = 0
#         cur_node = self.head
#         while cur_node:
#             total += 1
#             cur_node = cur_node.next
#         return total
#
#     def push(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             cur_node = self.head
#             while cur_node.next:
#                 cur_node = cur_node.next
#             cur_node.next = Node(data)
#
#     def unshift(self, data):
#         if self.head is None:
#             self.push(data)
#         new_node = Node(data, self.head)
#         self.head = new_node
#
#     def insert(self, index, data):
#         if index < 0 or index > self.length:
#             raise IndexError
#         elif index == 0:
#             self.unshift(data)
#         elif index == self.length:
#             self.push(data)
#         else:
#             count = 0
#             cur_node = self.head
#             while count < index - 1:
#                 cur_node = cur_node.next
#                 count += 1
#             cur_node.next = Node(data, cur_node.next)
#
#     def remove_beg(self):
#         if self.head is None:
#             raise ValueError
#         else:
#             self.head = self.head.next
#
#     def remove_end(self):
#         if self.head is None:
#             raise ValueError
#         else:
#             cur_node = self.head
#             while cur_node.next.next is not None:
#                 cur_node = cur_node.next
#             cur_node.next = None
#
#     def remove_at(self, index):
#         if index < 0 or index > self.length:
#             raise IndexError
#         elif index == 0:
#             self.remove_beg()
#         elif index == self.length:
#             self.remove_end()
#         else:
#             count = 0
#             cur_node = self.head
#             while count < index - 1:
#                 cur_node = cur_node.next
#                 count += 1
#             cur_node.next = cur_node.next.next
#
#
########################################################

# Double Linked List
#
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
# class DoubleLinkedList:
#     def __init__(self, head=None, end=None):
#         self.head = head
#         self.end = end
#
#     def display(self):
#         if self.head is None:
#             print('[]')
#         else:
#             elements = []
#             cur_node = self.head
#             while cur_node:
#                 elements.append(cur_node.data)
#                 cur_node = cur_node.next
#             print(elements)
#
#     def reverse(self):
#         if self.head is None:
#             print('[]')
#         else:
#             elements = []
#             cur_node = self.end
#             while cur_node:
#                 elements.append(cur_node.data)
#                 cur_node = cur_node.prev
#             print(elements)
#
#     @property
#     def length(self):
#         total = 0
#         cur_node = self.head
#         while cur_node:
#             cur_node = cur_node.next
#             total += 1
#         return total
#
#     def unshift(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.end = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#
#     def push(self, data):
#         if self.head is None:
#             self.unshift(data)
#         else:
#             new_node = Node(data, prev=self.end)
#             self.end.next = new_node
#             self.end = new_node
#
#     def insert(self, index, data):
#         if index < -1 or index > self.length:
#             raise IndexError('oops')
#         elif index == 0:
#             self.unshift(data)
#         elif index == -1 or index == self.length:
#             self.push(data)
#         else:
#             count = 0
#             cur_node = self.head
#             while count < index - 1:
#                 cur_node = cur_node.next
#                 count += 1
#             new_node = Node(data, prev=cur_node, next=cur_node.next)
#             cur_node.next = new_node
#             new_node.next.prev = new_node
#
#     def remove_start(self):
#         if self.head is None:
#             print('[]')
#         elif self.head == self.end:
#             self.head = None
#             self.end = None
#         else:
#             self.head.next = self.head
#             self.head.prev = None
#
#     def remove_end(self):
#         if self.head is None:
#             print('[]')
#         if self.head == self.end:
#             self.head = None
#             self.end = None
#         else:
#             self.end = self.end.prev
#             self.end.next = None
#
#     def remove_at(self, index):
#         if index < -1 or index > self.length:
#             raise IndexError('oops')
#         elif index == 0:
#             self.remove_start()
#         elif index == -1 or index == self.length:
#             self.remove_end()
#         else:
#             count = 0
#             cur_node = self.head
#             while count < index - 1:
#                 cur_node = cur_node.next
#                 count += 1
#             cur_node.next = cur_node.next.next
#             cur_node.next.prev = cur_node
#
#     def clear(self):
#         if self.head is None:
#             print('[]')
#         else:
#             cur_node = self.head
#             while cur_node:
#                 cur_node.prev = None
#                 cur_node = cur_node.next
#             self.head = None
#             self.end = None

########################################################

# Circular Double Linked List QUESTIONS!!!!
