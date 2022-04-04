class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def removeFromEndIndex(self,n):     #n is the position from the end of the linked list
        fast = slow = self.head
        for _ in range(n):
            fast=fast.next
        
