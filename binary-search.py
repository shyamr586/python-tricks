# binary search is important to search for elements in a short amount of time
# the Big O notation for binary search is O(log n), whereas the normal way of iterating through every element is
# O(n) (n is the number of elements of the variable), which takes more computation

def binarySearch(array):
    array.sort()                                          #the item to be searched using binary should always be sorted

    # if (array[len(array)/2])
    print(array[len(array)/2])

thelist = [1,2,3,4,5]
binarySearch(thelist)