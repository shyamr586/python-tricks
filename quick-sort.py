#this is an implementation of quick sort which has O(nlog n) complexity as best case and O(n^2) as worst case.
#worst case is when all elements are already sorted which means all elements have to be compared to each other.
def qSort(array):
    if (len(array)<=1):
        return array
    else:
        pivot = array.pop()     #removes last element as well as store it in pivot variable
                                #it is a convention to take the last element as pivot
        lesser = []
        greater = []
        for elem in array:
            if (elem<pivot):
                lesser.append(elem)
            else:
                greater.append(elem)
        return qSort(lesser)+[pivot]+qSort(greater) #recursion woooo, btw [pivot] so we convert elem to list to 
                                                    #make concatination possible

unsorted1 = [20,9,1,0,8,13]
unsorted2 = [2,3,6,1,0,13]

print (qSort(unsorted1))
print (qSort(unsorted2))