#just like selection sort, this sorting algo is also good for small arrays and is better than bubble sort.

def iSort(array):
    for i in range(1,len(array)):         #insertion sort compares the left with the rest thats why we start
                                          #loop with 1 and not 0. We assume 0th element is the smallest
        while (i>0 and array[i-1]>array[i]):
            array[i],array[i-1]=array[i-1],array[i]
            i-=1
    return array

unsorted1 = [20,9,1,0,8,13]
unsorted2 = [2,3,6,1,0,13]

print (iSort(unsorted1))
print (iSort(unsorted2))