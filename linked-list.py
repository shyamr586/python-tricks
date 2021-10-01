class Element(object):                      #these are the elements of the linked list, each element of the 
                                    #linked lists have a value and a address to the next element which
                                    #has default value None.
                                    #this class is sometimes called Node or ListNode
    def __init__(self,value):
        self.value = value
        self.next = None

#in the below class, i use 'current' var which means it is the current element of the list.
#usually used to iterate through the ll and takes value of head at first.

class LinkedList(object):                   #the linked lists use element class to initiate elements in the linked list.
                                    #it has one var, head, which basically is the first element of the ll.
    def __init__(self,head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if (self.head):             #if there is one element atleast in the list (which becames the head)
            while (current.next):   #to skip all elements which has a next value
                current = current.next
            current.next = new_element  #when the loop breaks it will create the new element as the last  
        else:
            self.head = new_element

    def insert(self,position,new_element):      #method to enter a element into a specified position where
                                                #head element is position 1
        current = self.head
        currpos = 1
        if (position == 1):
            self.head = new_element
            new_element.next = current
        else:
            while (current.next):
                if (currpos+1==position):
                    new_element.next = current.next
                    current.next = new_element
                currpos+=1
                current = current.next

    def printLength(self):
        len = 0
        current = self.head
        while (current):
            len+=1
            current = current.next
        print (len)

    def printList(self):
        current = self.head
        num = 0
        while (current):
            print("Element Number is:",num," Value: ", current.value," Next: ",current.next)
            current = current.next

    

#this is how an element is defined before putting in a linkedlist
e1 = "A"
e2 = "B"
e3 = "C"
E1 = Element(e1)
E2 = Element(e2)
E3 = Element(e3)

L = LinkedList(E1)
L.append(E2)
L.append(E3)

L.printList()
L.printLength()

E4 = Element("D")
L.insert(3,E4)
L.printList()
