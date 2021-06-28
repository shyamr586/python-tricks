# Python uses 'heap' data structure to implement priority queues.
# time complexity for inserting and deleting in a priority queue is: O(log n)
# https://www.geeksforgeeks.org/priority-queue-in-python/
# https://en.wikipedia.org/wiki/Heap_(data_structure)#:~:text=The%20heap%20is%20one%20maximally,always%20stored%20at%20the%20root.

# to check other ways of implementing a priority queue, check
# https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3

# The heap is one maximally efficient implementation of an abstract data type called a priority queue,
# and in fact, priority queues are often referred to as "heaps", regardless of 
# how they may be implemented. In a heap, the highest (or lowest) priority element is always stored at the root.

import heapq
# to use any heapq methods, access methods by: heapq.methodname(iterable item, optional-argument)

items = [50,23,1,75,20,3,13]

heapq.heapify(items)            # converts array to heap, always makes the smallest element be at index 0
                                # note that it does not return, so, x in x = heapq.heapify(array) will return None
print ("Items after heapify: "+str(items))

#heap methods need to have array as an argument
#inserting to a heap:
heapq.heappush(items, 7)
print ("Items after heappush: "+str(items))

#popping from a heap
heapq.heappop(items)            # pops the lowest element
print ("Items after heappop: "+str(items))

#replacing an element
heapq.heapreplace(items,0)      # replaces the lowest element with element specified in argument
print ("Items after heapreplace: "+str(items))

#to get n number of the smallest or highest elements of a list, we can use nsmallest and
#n highest which is supported in the heapq module
minthree = heapq.nsmallest(3, items)
maxthree = heapq.nlargest(3, items)
print ("Smallest three items in items: "+str(minthree))
print ("Highest three items in items: "+str(maxthree))

#https://docs.python.org/3/library/heapq.html