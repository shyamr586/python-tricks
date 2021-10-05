#merge sorts have complexity of O(n logn) and it is preferred to be used in a linked list.

def mSort(array):
    if (len(array)<=1):
        return array
    else:
        lefthalf = array[:len(array)//2]            #using / will give error because decimals
        righthalf = array[len(array)//2:]           #check splicing and stuff to know more about :
        
        mSort(lefthalf)                             #like mentioned in theory, the list has to be split first and
        mSort(righthalf)                            #then compared. Also, recursion woooo

        i,j = 0,0                                   #i is to iterate through lefthalf and j for righthalf
        k = 0                                       #this is for iterating through the merged array

        while (i<len(lefthalf) and j<len(righthalf)):   #to iterate through both arrays from start to end
            if (lefthalf[i] <righthalf[j]):
                array[k] = lefthalf[i]
                i+=1                                    #finished using that element, now next 
            else:
                array[k] = righthalf[j]
                j+=1                                    #finished using that element, now next 
            k+=1
        
        #without the next two blocks there can be duplicates of a value and other values may go missing.
        #assigns the remaining values because some of the values may not be traversed
        while (i<len(lefthalf)):
            array[k] = lefthalf[i]
            i+=1
            k+=1
        
        while (j<len(righthalf)):
            array[k] = righthalf[j]
            j+=1
            k+=1

        return array
unsorted1 = [20,9,1,0,8,13]
unsorted2 = [2,3,6,1,0,13]

print (mSort(unsorted1))
print (mSort(unsorted2))
