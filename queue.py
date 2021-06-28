# deque is used to implemet the 'queue' data structure in python
# it allows simple implementation of the FILO access of objects
# popping and adding to a queue only takes O(1) time complexity

from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

print ("-"*50)
print ("Original Queue:")
print ("-"*50+"\n")

print (str(q)+"\n")

popped = q.pop()

print ("-"*50)
print ("Using pop:")
print ("-"*50+"\n")

print("Popped: "+str(popped))
print("Q after pop: "+str(q)+"\n")

q.appendleft(0)

print ("-"*50)
print ("Using append left and pop left:")
print ("-"*50+"\n")

print(q)
popped = q.popleft()
print ("Left popped: "+str(popped))
print ("Q after left popped: "+str(q)+"\n")

# q = deque([1,4,23,5])                 # use something like this to convert array to queue
# q = deque("Hello")                    # works with iterables like strings 