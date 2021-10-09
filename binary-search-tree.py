class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root,new_val)
    
    def insert_helper(self,curr,new_val):
        if curr.value<new_val:
            if curr.left:
                self.insert_helper(curr.left,new_val)
            else:
                curr.left = Node(new_val)
        else:
            if curr.right:
                self.insert_helper(curr.right,new_val)
            else:
                curr.right = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root,find_val)
        
    def search_helper(self,curr,find_val):
        if curr:
            if curr.value == find_val:
                return True
            elif find_val<curr.value:
                self.search_helper(curr.left,find_val)
            else:
                self.search_helper(curr.left,find_val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))