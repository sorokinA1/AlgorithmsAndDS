# Python code to delete a node in AVL tree
# Generic tree node class
# https://www.cs.usfca.edu/~galles/visualization/AVLtree.html !!!
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports insertion,
# deletion operations
class AVL_Tree:
    def insert(self, root, data):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        # Case 2 - Right Right
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        # Case 3 - Left Right
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Case 4 - Right Left
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Recursive function to delete a node with
    # given data from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, node):
        if root is None:
            return root
        if node > root.data:
            root.right = self.delete(root.right, node)
        elif node < root.data:
            root.left = self.delete(root.left, node)
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
            root.right = self.delete(root.right, root.data)

        # If the tree has only one node,
        # simply return it
        if root is None:
            return root

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Case 2 - Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Case 3 - Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Case 4 - Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_left(self, grand_parent):
        print('Rotating to the left on node:', grand_parent.data)
        temp = grand_parent.right
        grand_parent.right = temp.left

        # Perform rotation
        temp.left = grand_parent

        # Update heights
        grand_parent.height = 1 + max(self.get_height(grand_parent.left),
                                      self.get_height(grand_parent.right))
        temp.height = 1 + max(self.get_height(temp.left),
                              self.get_height(temp.right))

        # Return the new root
        return temp

    def rotate_right(self, grand_parent):
        print('Rotating to the right on node:', grand_parent.data)
        temp = grand_parent.left
        grand_parent.left = temp.right

        # Perform rotation
        temp.right = grand_parent

        # Update heights
        grand_parent.height = 1 + max(self.get_height(grand_parent.left),
                                      self.get_height(grand_parent.right))
        temp.height = 1 + max(self.get_height(temp.left),
                              self.get_height(temp.right))

        # Return the new root
        return temp

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min_value(root.left)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


myTree = AVL_Tree()
root = None
nums = [10, 20, 5, 6, 15]

for num in nums:
    root = myTree.insert(root, num)

# Preorder Traversal
print("Preorder Traversal after insertion -")
myTree.preOrder(root)
print()

# Delete
root = myTree.delete(root, 15)
root = myTree.delete(root, 20)

# Preorder Traversal
print("Preorder Traversal after deletion -")
myTree.preOrder(root)
