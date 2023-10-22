# from Linked_list import LinkedList

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.data) for x in self.linked_list]
        return ' -> '.join(values)

    @property
    def is_empty(self):
        return True if self.linked_list.head is None else False

    def push(self, data):
        new_node = Node(data)
        if self.linked_list.head is None:
            self.linked_list.head = Node(data)
        else:
            new_node.next = self.linked_list.head
            self.linked_list.head = new_node

    def pop(self):
        if self.is_empty:
            print('[]')
        else:
            node_data = self.linked_list.head.next
            self.linked_list.head = self.linked_list.head.next
            return node_data

    def peek(self):
        if self.is_empty:
            print('[]')
        else:
            return self.linked_list.head.data

    def clear(self):
        self.linked_list.head = None


new_stack = Stack()
print(new_stack.is_empty)
new_stack.push('Sayaka')
new_stack.push('Sakura')
new_stack.push('Haru')
new_stack.push('Yui')
print(new_stack)
new_stack.pop()
print(new_stack)
print(new_stack.peek())


