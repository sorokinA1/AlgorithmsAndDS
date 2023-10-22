#                                5
#                             /     \
#                            3       7
#                           / \     / \
#                          2   4   6   9

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, cur_node, data):
        if data <= cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(cur_node.left, data)

        if data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(cur_node.right, data)

    def find(self, data):
        if self.root:
            is_found = self._find(self.root, data)
            return True if is_found else False
        else:
            return None

    def _find(self, cur_node, data):
        if data > cur_node.data and cur_node.right:
            return self._find(cur_node.right, data)
        elif data < cur_node.data and cur_node.left:
            return self._find(cur_node.left, data)
        if data == cur_node.data:
            return True

    def pre_order_print(self, cur_node, traversal):
        if cur_node:
            traversal += str(cur_node.data) + '-'
            traversal = self.pre_order_print(cur_node.left, traversal)
            traversal = self.pre_order_print(cur_node.right, traversal)
        return traversal

    def delete_node(self, root, node):
        if root is None:
            return root
        #                                5
        #                             /     \
        #                            3       7
        #                           / \     / \
        #                          2   4   6   9
        #                         / \ / \ / \ / \
        # https://www.youtube.com/watch?v=LFzAoJJt92M
        if node > root.data:
            root.right = self.delete_node(root.right, node)
        elif node < root.data:
            root.left = self.delete_node(root.left, node)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # find the min from right subtree
            cur_node = root.right
            while cur_node.left:
                cur_node = cur_node.left
            root.data = cur_node.data
            root.right = self.delete_node(root.right, root.data)
        return root


tree = BST()
tree.insert(1)
tree.insert(2)
tree.insert(3)
print(tree.pre_order_print(tree.root, '->'))
print(tree.find(4))
tree.delete_node(tree.root, 3)
print(tree.pre_order_print(tree.root, '->'))
