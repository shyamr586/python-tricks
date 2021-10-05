#bubble sort isnt the best sorting algo but its used to learn sorting methodology. 

def bSort(array):
    issorted = False
    while (not issorted):
        issorted = True
        for i in range(len(array)-1):
            if (array[i]>array[i+1]):
                array[i],array[i+1]=array[i+1],array[i]     #change both elements simultaneously
                issorted = False                            #when there is no change, issorted stays true and the 
                                                            #loop will break and return sorted array
    return array
            
           
unsorted1 = [20,9,1,0,8,13]
unsorted2 = [2,3,6,1,0,13]

print (bSort(unsorted1))
print (bSort(unsorted2))