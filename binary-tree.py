#binary tree is like a linked list but it will have a left and right node connection instead of a next like in LL.
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):         #we call this method from main because we wont know root of the tree
                                       
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):               #same reason, we wont know root of tree.
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):  #the course calls it a helper function because we can call it 
                                                 #recursively
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)  
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print( tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())