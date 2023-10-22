# https://www.youtube.com/watch?v=JlMyYuY1aXU
# https://github.com/bfaure/Python3_Data_Structures/blob/master/Linked_List/main.py

# https://www.youtube.com/watch?v=B-zO18TJKYQ        part - 1
# https://www.youtube.com/watch?v=o8tWJCFWEPU&t=1s   part - 2
# https://www.youtube.com/watch?v=enRNwavYa9U        part - 3


##############################################################
# https://www.youtube.com/watch?v=qp8u-frRAnU&t=1151s THE BEST!
##############################################################

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def display(self):
        if self.head is None:
            print('[]')
        else:
            elements = []
            cur_node = self.head
            while cur_node:
                elements.append(cur_node.data)
                cur_node = cur_node.next
            print(elements)

    @property
    def length(self):
        total = 0
        cur_node = self.head
        while cur_node:
            total += 1
            cur_node = cur_node.next
        return total

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(data)

    def unshift(self, data):
        if self.head is None:
            self.push(data)
        new_node = Node(data, self.head)
        self.head = new_node

    def insert(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError
        elif index == 0:
            self.unshift(data)
        elif index == self.length:
            self.push(data)
        else:
            count = 0
            cur_node = self.head
            while count < index - 1:
                cur_node = cur_node.next
                count += 1
            cur_node.next = Node(data, cur_node.next)

    def remove_beg(self):
        if self.head is None:
            raise ValueError
        else:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            raise ValueError
        else:
            cur_node = self.head
            while cur_node.next.next is not None:
                cur_node = cur_node.next
            cur_node.next = None

    def remove_at(self, index):
        if index < 0 or index > self.length:
            raise IndexError
        elif index == 0:
            self.remove_beg()
        elif index == self.length:
            self.remove_end()
        else:
            count = 0
            cur_node = self.head
            while count < index - 1:
                cur_node = cur_node.next
                count += 1
            cur_node.next = cur_node.next.next
#########################################################
