#                                5
#                             /     \
#                            3       7
#                           / \     / \
#                          2   4   6   9

from Queue.queue_practice import Queue


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, cur_node, data):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(cur_node.left, data)

        if data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(cur_node.right, data)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self._pre_order_print(self.root, '->')
        elif traversal_type == 'inorder':
            return self._in_order_print(self.root, '->')
        elif traversal_type == 'postorder':
            return self._post_order_print(self.root, '->')
        elif traversal_type == 'levelorder':
            return self._level_order_print(self.root)
        else:
            return 'operation is not supported'

    def _pre_order_print(self, root, traversal):
        if root:
            traversal += str(root.data) + '-'
            traversal = self._pre_order_print(root.left, traversal)
            traversal = self._pre_order_print(root.right, traversal)
        return traversal

    def _in_order_print(self, root, traversal):
        if root:
            traversal = self._in_order_print(root.left, traversal)
            traversal += str(root.data) + '-'
            traversal = self._in_order_print(root.right, traversal)
        return traversal

    def _post_order_print(self, root, traversal):
        if root:
            traversal = self._post_order_print(root.left, traversal)
            traversal = self._post_order_print(root.right, traversal)
            traversal += str(root.data) + '-'
        return traversal

    def _level_order_print(self, root):
        if root:
            queue = Queue(10)
            queue.enqueue(root)
            traversal = '->'
            while not queue.isEmpty:
                traversal += str(queue.showFront()) + '-'
                node = queue.dequeue()

                if node.data.left:
                    queue.enqueue(node.data.left)
                if node.data.right:
                    queue.enqueue(node.data.right)
            return traversal

    def delete_node(self, root, node):
        if root is None:
            return root

        if node > root.data:
            root.right = self.delete_node(root.right, node)
        elif node < root.data:
            root.left = self.delete_node(root.left, node)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            cur_node = root.right
            while cur_node.left:
                cur_node = cur_node.left
            root.data = cur_node
            root.right = self.delete_node(root.right, root.data)
        return root

        #                                5
        #                             /     \
        #                            3       7
        #                           / \     / \
        #                          2   4   6   9
        #                         / \ / \ / \ / \
        #                                    x   y


tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(9)
print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))
print(tree.print_tree('levelorder'))
tree.delete_node(tree.root, 3)
print(tree.print_tree('levelorder'))
