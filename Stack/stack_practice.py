# new_stack = []
# new_stack.append('Artem')
# new_stack.append('Polina')
# new_stack.append('Villanelle')
#
# print(new_stack)
# print(new_stack[-1])
# new_stack.pop()
# print(new_stack)
# new_stack.clear()
# print(new_stack)

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
        if self.is_empty:
            self.linked_list.head = new_node
        else:
            new_node.next = self.linked_list.head
            self.linked_list.head = new_node

    def pop(self):
        if self.is_empty:
            print('[]')
        else:
            node = self.linked_list.head.data
            self.linked_list.head = self.linked_list.head.next
            return node

    def peek(self):
        if not self.is_empty:
            return self.linked_list.head.data
        else:
            print('[]')

    def clear(self):
        self.linked_list.head = None


new_stack = Stack()
new_stack.push('Artem')
new_stack.push('Polina')
new_stack.push('Amber')
print(new_stack)
new_stack.pop()
print(new_stack)
print(new_stack.peek())
