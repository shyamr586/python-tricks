
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    # def print_val(self):
    #     print (self.value)

class BinaryTree:
    def __init__(self,root):
        self.root = root

    def insert_node(self,to_add):
        self.insert_helper(to_add,self.root)

    def insert_helper(self,to_add,curr_node):
        current = curr_node
        value = to_add.value
        if (current):
            if (value<current.value):
                if (current.left):
                    self.insert_helper(to_add,current.left)
                else:
                    current.left = to_add
            else:
                if (current.right):
                    self.insert_helper(to_add,current.right)
                else:
                    current.right = to_add
        else:
            current = to_add

    def print_tree(self):
        self.print_helper(self.root,1,"no direciton, this is root")

    def print_helper(self,current,level,direction):
        print ("Level",level," is: ",current.value,"direction: ",direction)
        if (current.left):
            self.print_helper(current.left,level+1,"left")
        if (current.right):
            self.print_helper(current.right,level+1,"right")

N1 = Node(5)
N2 = Node(2)
N3 = Node(10)
N4 = Node(20)
N5 = Node(15)

T = BinaryTree(N1)
T.insert_node(N2)
T.insert_node(N3)
T.insert_node(N4)
T.insert_node(N5)

T.print_tree()