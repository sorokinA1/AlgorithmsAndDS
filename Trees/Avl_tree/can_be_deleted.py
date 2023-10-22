class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    def insert(self, root, data):
        if not root:
            return Node(data)

        elif data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.calc_height(root.left),
                              self.calc_height(root.right))

        balance = self.calc_balance(root)

        if balance > 1 and data < root.left.data:
            print('Left left havey...')
            return self.rotate_right(root)

        if balance < -1 and data > root.right.data:
            print('Right right heavy...')
            return self.rotate_right(root)

        if balance > 1 and data > root.left.data:
            print('Left right heavy...')
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance > -1 and data < root.right.data:
            print('Right left heavy...')
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def remove(self, root, node):


    def calc_height(self, root):
        if not root:
            return 0
        else:
            return root.height

    def calc_balance(self, root):
        if not root:
            return 0
        else:
            return self.calc_height(root.left) - self.calc_height(root.right)

    def rotate_left(self, grand_parent):
        print('Rotating to the left node:', grand_parent)

        temp = grand_parent.right
        grand_parent.right = temp.left
        temp.left = grand_parent

        grand_parent.height = 1 + max(self.calc_height(grand_parent.right),
                                      self.calc_height(grand_parent.left))
        temp.height = 1 + max(self.calc_height(temp.right),
                              self.calc_height(temp.left))

        return temp

    def rotate_right(self, grand_parent):
        print('Rotating to the right node:', grand_parent)

        temp = grand_parent.left
        grand_parent.left = temp.right
        temp.right = grand_parent

        grand_parent.height = 1 + max(self.calc_height(grand_parent.right),
                                      self.calc_height(grand_parent.left))
        temp.height = 1 + max(self.calc_height(temp.right),
                              self.calc_height(temp.left))

        return temp

    def pre_order_print(self, cur_node, traversal):
        if cur_node:
            traversal += str(cur_node.data) + '-'
            traversal = self.pre_order_print(cur_node.left, traversal)
            traversal = self.pre_order_print(cur_node.right, traversal)
        return traversal

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


myTree = AvlTree()
root = None
nums = [10, 20, 5, 6, 15]

for num in nums:
    root = myTree.insert(root, num)

myTree.preOrder(root)
