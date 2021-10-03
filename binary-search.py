# binary search is important to search for elements in a short amount of time
# the Big O notation for binary search is O(log n), whereas the normal way of iterating through every element is
# O(n) (n is the number of elements of the variable), which takes more computation

def binarySearch(array,val):
    array.sort()                                          #the item to be searched using binary should always be sorted
    low = 0                                               #starting index, always 0
    high = len(array)-1                                   #ending index, len - 1
    while (low<=high):                                    #as long as the low index doesnt exceed high index
        mid = (low+high)/2                                #calc mid to split the list in a way
        if (array[mid]==val):                             #if the middle value is the value
            return mid                                    #just return the middle index number
        elif (array[mid]<val):
            low = mid + 1                                 #if the mid value is low, adjust the lower value to be 
                                                          #the first index in the second half
        else:
            high = mid - 1                                #if the mid value is high, adjust the higher value to be
                                                          #the last index of the first half
    return -1                                             #not found condition

thelist = [1,2,3,4,5]
value = 3
binarySearch(thelist,value)