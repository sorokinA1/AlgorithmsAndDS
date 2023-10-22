#
#                                1
#                             /     \
#                            2       3
#                           / \     / \
#                          4   5   6   7

from Queue.queue_practice import Queue


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self._preorder_print(self.root, '-> ')
        elif traversal_type == 'inorder':
            return self._inorder_print(self.root, '-> ')
        elif traversal_type == 'postorder':
            return self._post_order_print(self.root, '->')
        elif traversal_type == 'levelorder':
            return self._level_order_print(self.root)
        else:
            'this type is not supported'

    def _preorder_print(self, cur_node, traversal):
        if cur_node:
            traversal += str(cur_node.data) + '-'
            traversal = self._preorder_print(cur_node.left, traversal)
            traversal = self._preorder_print(cur_node.right, traversal)
        return traversal

    def _inorder_print(self, cur_node, traversal):
        if cur_node:
            traversal = self._inorder_print(cur_node.left, traversal)
            traversal += str(cur_node.data) + '-'
            traversal = self._inorder_print(cur_node.right, traversal)
        return traversal

    def _post_order_print(self, cur_node, traversal):
        if cur_node:
            traversal = self._post_order_print(cur_node.left, traversal)
            traversal = self._post_order_print(cur_node.right, traversal)
            traversal += str(cur_node.data) + '-'
        return traversal

    def _level_order_print(self, cur_node):
        if cur_node:
            my_queue = Queue(10)
            my_queue.enqueue(cur_node)
            traversal = ''

            while not my_queue.isEmpty:
                traversal += str(my_queue.showFront()) + '-'
                node = my_queue.dequeue()

                if node.data.left:
                    my_queue.enqueue(node.data.left)
                if node.data.right:
                    my_queue.enqueue(node.data.right)
            return traversal

    def find_node(self, cur_node, needed_node):
        if cur_node:
            new_queue = Queue(10)
            new_queue.enqueue(cur_node)

            while not new_queue.isEmpty:
                node = new_queue.dequeue()

                if str(node) == str(needed_node):
                    return needed_node
                if node.data.left:
                    new_queue.enqueue(node.data.left)
                if node.data.right:
                    new_queue.enqueue(node.data.right)
            return 'not found'

    def insert_node(self, root_node, new_node):
        if not self.root:
            self.root = TreeNode(root_node)
        else:
            my_queue = Queue(10)
            my_queue.enqueue(root_node)

            while not my_queue.isEmpty:
                node = my_queue.dequeue()

                if node.data.left:
                    my_queue.enqueue(node.data.left)
                else:
                    node.data.left = TreeNode(new_node)
                    return

                if node.data.right:
                    my_queue.enqueue(node.data.right)
                else:
                    node.data.right = TreeNode(new_node)
                    return

    def get_deepest_node(self, root_node):
        new_queue = Queue(10)
        new_queue.enqueue(root_node)

        while not new_queue.isEmpty:
            node = new_queue.dequeue()
            if node.data.left:
                new_queue.enqueue(node.data.left)
            if node.data.right:
                new_queue.enqueue(node.data.right)

        deepest_node = node.data
        return deepest_node


tree = BinaryTree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)
print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))
print(tree.print_tree('levelorder'))
print(tree.find_node(tree.root, 8))
tree.insert_node(tree.root, 8)
print(tree.print_tree('levelorder'))
print(tree.get_deepest_node(tree.root))
