class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.bst_insert(self.root, new_val)

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def print_bst_traversal(self, find_val):
        return self.bst_print(self.root, find_val, "")[:-1]

    def bst_insert(self, start, new_val):

        if start.value > new_val:
            if not start.left:
                start.left = Node(new_val)
            else:
                return self.bst_insert(start.left, new_val)

        elif start.value < new_val:
            if not start.right:
                start.right = Node(new_val)
            else:
                return self.bst_insert(start.right, new_val)

    def bst_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                if start.value > find_val:
                    self.bst_search(start.left, find_val)
                elif start.value < find_val:
                    self.bst_search(start.right, find_val)
        return False

    def bst_print(self, start, find_val, traversal):
        if start:
            traversal += str(start.value) + "-"
            if start.value > find_val:
                traversal = self.bst_print(start.left, find_val, traversal)
            elif start.value < find_val:
                traversal = self.bst_print(start.right, find_val, traversal)
        return traversal


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
# tree.insert(6)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
# print(tree.print_bst_traversal(6))