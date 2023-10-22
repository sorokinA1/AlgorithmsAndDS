# https://www.youtube.com/watch?v=Y-nmgO8ALjM best
# intro to AVL https://www.youtube.com/watch?v=-9sHvAnLN_w&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=60
# Node -> https://www.youtube.com/watch?v=aGBjLRbaC6M&list=PL1SWSsc5Gso_Cw5Pj2_IAAGuyio0O1x3o&index=44
# Height -> https://www.youtube.com/watch?v=sCXT6XE8sxg
# Rotation -> https://www.youtube.com/watch?v=4biU2w7T8Ek&t=118s
# Insertion https://www.youtube.com/watch?v=yWGU_vmTh6w&list=PL1SWSsc5Gso_Cw5Pj2_IAAGuyio0O1x3o&index=46
# Tree Rebalance -> https://www.youtube.com/watch?v=9w7yP0or8tM&list=PL1SWSsc5Gso_Cw5Pj2_IAAGuyio0O1x3o&index=39
# !!! https://github.com/anujdutt9/Python-Data-Structures-and-Algorithms/blob/master/AVL_Tree/AVLTree.py
# https://www.youtube.com/watch?v=vH8SKx5lFEQ&list=PL1SWSsc5Gso_Cw5Pj2_IAAGuyio0O1x3o&index=32
# https://www.youtube.com/watch?v=U1JYwHcFfso MIT avl tree
######################################################################


# AVL Tree
# On every insertion check if tree is balanced or not using height
# If it is unbalanced, make rotation to balance it


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None  # Left Child to current node
        self.right = None  # Right child to current node
        self.height = 0  # Height of Tree to make sure tree is balanced


# Perform operations on AVL Tree
class AVL:
    def __init__(self):
        self.root = None  # Root Node

    # --------------------------- Calculate Height of AVL Tree ---------------------------------
    def calc_height(self, node):
        if not node:  # If this Node is Null
            return -1  # return -1; left and right child of leaf Nodes
        # print('\nHeight: ', node.height)
        return node.height

    # ------------------------------- Insertion of Node in a AVL Tree ----------------------------
    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if node is None:  # If it is a root node, create a new node
            return Node(data)
        if data < node.data:  # If data < current node, go to left else right
            node.left = self.insert_node(data, node.left)
        else:
            node.right = self.insert_node(data, node.right)
        # Get the height of the new node
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        # Node has been inserted.
        # Now check if there has been any violations of AVL Tree
        # print('Node {} Inserted'.format(data))
        return self.set_balance(data, node)

    # -------------------- Settle any Violations upon adding/inserting new Node --------------------------
    def set_balance(self, data, node):
        balance = self.calc_balance(node)
        # Case 1: Left Left Heavy situation
        if balance > 1 and data < node.left.data:
            print("Left Left Heavy Situation...")
            return self.rotate_right(node)
        # Case 2: Right Right Heavy Situation
        if balance < -1 and data > node.right.data:
            print('Right Right Heavy Situation...')
            return self.rotate_left(node)
        # Case 3: Left Right Heavy Situation
        if balance > 1 and data > node.left.data:
            print('Left Right Heavy Situation...')
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Case 4: Right Left Heavy Situation
        if balance < -1 and data < node.right.data:
            print('Right Left Heavy Situation...')
            node.right = self.rotate_right(node.right)  # Here node is the Root Node
            return self.rotate_left(node)
        return node

    # ------------------------------- See if Tree is Balanced or not -------------------------------
    # If it returns value > 1, it means it is a Left heavy tree
    # Make Right rotation to balance it
    # If it returns value < 1, it means it is a Right heavy tree
    # Make Left rotation to balance it
    def calc_balance(self, node):
        if not node:
            return 0
        return self.calc_height(node.left) - self.calc_height(node.right)

    # Rotate Nodes to Right to Balance AVL Tree
    # O(1) time Complexity
    def rotate_right(self, grand_parent):
        print('Rotating to the right on node:', grand_parent.data)

        temp = grand_parent.left
        grand_parent.left = temp.right
        temp.right = grand_parent

        grand_parent.height = max(self.calc_height(grand_parent.left),
                                  self.calc_height(grand_parent.right)) + 1

        temp.height = max(self.calc_height(temp.left),
                          self.calc_height(temp.right)) + 1

        return temp

    # Rotate Nodes to Left to Balance AVL Tree
    # O(1) time Complexity
    def rotate_left(self, grand_parent):
        print('Rotating to the left on node:', grand_parent.data)

        temp = grand_parent.right
        grand_parent.right = temp.left
        temp.left = grand_parent

        grand_parent.height = max(self.calc_height(grand_parent.left),
                                  self.calc_height(grand_parent.right)) + 1

        temp.height = max(self.calc_height(temp.left),
                          self.calc_height(temp.right)) + 1

        return temp

    # ------------------------------ Remove Node from AVL Tree -----------------------
    # Remove Node [Deletion]
    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self.remove_node(data, node.left)
        if data > node.data:
            node.right = self.remove_node(data, node.right)
        else:
            if node.left is None and node.right is None:
                print('Removing a leaf node...')
                del node
                return None
            if node.left is None:
                print('Removing right child...')
                temp = node.right
                del node
                return temp
            if node.right is None:
                print('Removing left child...')
                temp = node.left
                return temp
            print('Removing Node with two children...')
            temp = self.get_predecessor(node.left)
            node.data = temp.data
            node.left = self.remove_node(temp.data, node.left)

        if node is None:
            return node
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        balance = self.calc_balance(node)

        # Doubly Left Heavy Tree
        if balance > 1 and self.calc_balance(node.left) >= 0:
            return self.rotate_right(node)
        # Doubly Right Heavy Tree
        if balance < -1 and self.calc_balance(node.right) <= 0:
            return self.rotate_left(node)
        # Left Right Case
        if balance > 1 and self.calc_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right Left Case
        if balance < -1 and self.calc_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

    # --------------------- Traverse the AVL Tree ------------------

    def inorder_print(self, cur_node, traversal):
        if cur_node:
            traversal = self.inorder_print(cur_node.left, traversal)
            traversal += str(cur_node.data) + '-'
            traversal = self.inorder_print(cur_node.right, traversal)
        return traversal


# ------------------- Testing -----------------
if __name__ == '__main__':
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(5)
    avl.insert(6)
    avl.insert(15)
    print(avl.inorder_print(avl.root, '->'))

    avl.remove(5)
    # avl.remove(20)
    print(avl.inorder_print(avl.root, '->'))
#       10
#     /    \
#    5      20
#  /       /
# 4      15
