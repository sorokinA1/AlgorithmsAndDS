class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self, level=0):
        spaces = '   ' * level + str(self.data) + '\n'
        for child in self.children:
            spaces += child.__str__(level + 1)
        return spaces

    def add_child(self, tree_node):
        self.children.append(tree_node)


tree = TreeNode('Drinks')
cold = TreeNode('Cold')
hot = TreeNode('Hot')
tree.add_child(cold)
tree.add_child(hot)
coffee = TreeNode('Coffee')
tea = TreeNode('Tea')
cola = TreeNode('Cola')
fanta = TreeNode('Fanta')
cold.add_child(cola)
cold.add_child(fanta)
hot.add_child(tea)
hot.add_child(coffee)
print(tree)

########################################################################
