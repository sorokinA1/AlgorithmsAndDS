# https://www.youtube.com/watch?v=LrCAokPC12g&t=116s
# https://www.youtube.com/watch?v=galDq38nlWg
# udemy is ok

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

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

    def reverse(self):
        if self.head is None:
            print('[]')
        else:
            elements = []
            cur_node = self.end
            while cur_node:
                elements.append(cur_node.data)
                cur_node = cur_node.prev
            print(elements)

    @property
    def length(self):
        total = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            total += 1
        return total

    def unshift(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push(self, data):
        if self.head is None:
            self.unshift(data)
        else:
            new_node = Node(data, prev=self.end)
            self.end.next = new_node
            self.end = new_node

    def insert(self, index, data):
        if index < -1 or index > self.length:
            raise IndexError('oops')
        elif index == 0:
            self.unshift(data)
        elif index == self.length or index == -1:
            self.push(data)
        else:
            count = 0
            cur_node = self.head
            while count < index - 1:
                cur_node = cur_node.next
                count += 1
            new_node = Node(data, prev=cur_node, next=cur_node.next)
            cur_node.next = new_node
            new_node.next.prev = new_node

    def search(self, data):
        if self.head is None:
            return '[]'
        else:
            cur_node = self.head
            while cur_node:
                if cur_node.data == data:
                    return cur_node.data
                cur_node = cur_node.next
            return 'not found'

    def remove_start(self):
        if self.head is None:
            print('[]')
        elif self.head == self.end:
            self.head = None
            self.end = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_end(self):
        if self.head is None:
            print('[]')
        elif self.head == self.end:
            self.head = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None

    def remove(self, index):
        if index < -1 or index > self.length:
            raise IndexError
        elif index == 0:
            self.remove_start()
        elif self.head == self.end:
            self.remove_end()
        elif index == self.length or index == -1:
            self.remove_end()
        else:
            count = 0
            cur_node = self.head
            while count < index - 1:
                cur_node = cur_node.next
                count += 1
            cur_node.next = cur_node.next.next
            cur_node.next.prev = cur_node

    def clear(self):
        if self.head is None:
            print('[]')
        else:
            cur_node = self.head
            while cur_node:
                cur_node.prev = None
                cur_node = cur_node.next
            self.head = None
            self.end = None


#########################################################

my_list = DoubleLinkedList()
my_list.unshift('Sayaka')
my_list.unshift('Sakura')
my_list.unshift('Akari')
my_list.push('Haru')
my_list.push('Yui')
my_list.push('Yukino')
my_list.insert(2, 'Polina')
my_list.insert(3, 'Asahi')
my_list.display()
my_list.reverse()
my_list.remove(2)
my_list.remove(0)
my_list.remove(-1)
my_list.display()
my_list.reverse()
my_list.clear()
my_list.display()
my_list.push('hi')
my_list.display()
print(my_list.length)
