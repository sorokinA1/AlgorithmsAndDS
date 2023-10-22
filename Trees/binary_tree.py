################################ PreOrder traversal #####################################
################################ InOrder traversal  #####################################
################################ PostOrder traversal  ###################################
################################ LevelOrder traversal  ##################################
#########################################################################################
# https://www.youtube.com/watch?v=_IhTp8q0Mm0 Code Beauty
# https://www.youtube.com/watch?v=6oL-0TdVy28 Good
# https://www.youtube.com/watch?v=4Xo-GtBiQN0 visual
# https://www.youtube.com/watch?v=aM-oswPn19o level order
# https://www.youtube.com/watch?v=76dhtgZt38A !! MIT
#
#                                1
#                             /     \
#                            2       3
#                           / \     / \
#                          4   5   6   7

# from Queue import Queue
#
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def __str__(self):
#         return str(self.data)
#
#
# class BinaryTree:
#     def __init__(self, root):
#         self.root = TreeNode(root)
#
#     def print_tree(self, traversal_type):
#         if traversal_type == 'preorder':
#             return self._preorder_print(self.root, '-> ')
#         elif traversal_type == 'inorder':
#             return self._inorder_print(self.root, '->')
#         elif traversal_type == 'postorder':
#             return self._post_order_print(self.root, '->')
#         elif traversal_type == 'levelorder':
#             return self._level_order_print(self.root)
#         else:
#             'this type is not supported'
#
#     def _preorder_print(self, cur_node, traversal):
#         """Root->Left->Right -> 1-2-4-5-3-6-7-"""
#         #                                1    DLR
#         #                             /     \
#         #                            2       3
#         #                           / \     / \
#         #                          4   5   6   7
#         if cur_node:  # base case
#             traversal += str(cur_node.data) + '-'
#             traversal = self._preorder_print(cur_node.left, traversal)
#             traversal = self._preorder_print(cur_node.right, traversal)
#         return traversal
#
#     def _inorder_print(self, cur_node, traversal):
#         """Left->Root->Right ->4-2-5-1-6-3-7-"""
#         #                                1    LRD
#         #                             /     \
#         #                            2       3
#         #                           / \     / \
#         #                          4   5   6   7
#         if cur_node:
#             traversal = self._inorder_print(cur_node.left, traversal)
#             traversal += str(cur_node.data) + '-'
#             traversal = self._inorder_print(cur_node.right, traversal)
#         return traversal
#
#     def _post_order_print(self, cur_node, traversal):
#         """Left->Right->Root ->4-5-2-6-7-3-1-"""
#         #                                1     LRD
#         #                             /     \
#         #                            2       3
#         #                           / \     / \
#         #                          4   5   6   7
#         if cur_node:
#             traversal = self._post_order_print(cur_node.left, traversal)
#             traversal = self._post_order_print(cur_node.right, traversal)
#             traversal += str(cur_node.data) + '-'
#         return traversal
#
#     def _level_order_print(self, cur_node):
#         # 1-q2-q3-q4-q5-q6-q7
#         #                                1
#         #                             /     \
#         #                            2       3
#         #                           / \     / \
#         #                          4   5   6   7
#
#         if cur_node is None:
#             return
#         else:
#             queue = Queue()
#             queue.enqueue(cur_node)
#
#             traversal = ''
#             while not queue.is_empty:
#                 traversal += str(queue.peek()) + '-'
#                 node = queue.dequeue()
#
#                 if node.left:
#                     queue.enqueue(node.left)
#                 if node.right:
#                     queue.enqueue(node.right)
#
#             return traversal
#
#
# tree = BinaryTree(1)
# tree.root.left = TreeNode(2)
# tree.root.right = TreeNode(3)
# tree.root.left.left = TreeNode(4)
# tree.root.left.right = TreeNode(5)
# tree.root.right.left = TreeNode(6)
# tree.root.right.right = TreeNode(7)
# print(tree.print_tree('levelorder'))


############################## With Circular linked list queue ##########################
##############################          more methods           ##########################
#########################################################################################
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
            my_queue = Queue(7)
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

    ######################################################################
    #################### LEVEL ORDER METHODS #####################
    ######################################################################

    def find_node(self, start, needed_node):
        if start:
            new_queue = Queue(7)
            new_queue.enqueue(start)

            while not new_queue.isEmpty:
                node = new_queue.dequeue()
                if str(node.data) == str(needed_node):
                    return needed_node
                if node.data.left:
                    new_queue.enqueue(node.data.left)
                if node.data.right:
                    new_queue.enqueue(node.data.right)
            return 'not found'

    def insert_node(self, root_node, new_node):
        if not root_node:
            self.root = TreeNode(new_node)
        else:
            new_queue = Queue(10)
            new_queue.enqueue(root_node)

            while not new_queue.isEmpty:
                node = new_queue.dequeue()
                if node.data.left:
                    new_queue.enqueue(node.data.left)
                else:
                    node.data.left = TreeNode(new_node)
                    return

                if node.data.right:
                    new_queue.enqueue(node.data.right)
                else:
                    node.data.right = TreeNode(new_node)
                    return

    def get_the_deepest(self, start):
        new_queue = Queue(7)
        new_queue.enqueue(start)

        while not new_queue.isEmpty:
            node = new_queue.dequeue()
            if node.data.left:
                new_queue.enqueue(node.data.left)
            if node.data.right:
                new_queue.enqueue(node.data.right)

        deepest_node = node.data
        return deepest_node

    def clear_tree(self, root_node):
        root_node.data = None
        root_node.left = None
        root_node.right = None


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
print(tree.get_the_deepest(tree.root))
tree.clear_tree(tree.root)
