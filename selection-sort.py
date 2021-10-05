#this one is better than a bubble sort because it doesnt need to iterate through every element in each pass.
#but, the complexity is still O(n^2) because we iterate through same list twice.
#Some people use this to take less space compared to other algo because space complexity is O(1).

def sSort(array):
    
    for i in range(len(array)-1):               #len(array)-1 because the last item is assumed to be the large value
                                                #removing -1 does not change the result but i guess it may take
                                                #slightly more time because of one more iteration.
        minindex = i
        for j in range(i+1,len(array)):
            if (array[j]<array[minindex]):
                minindex = j
    
        if (minindex!=i):
            array[minindex],array[i] = array[i],array[minindex]
    return array

unsorted1 = [20,9,1,0,8,13]
unsorted2 = [2,3,6,1,0,13]

print (sSort(unsorted1))
print (sSort(unsorted2))