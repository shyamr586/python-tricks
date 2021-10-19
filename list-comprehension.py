# in order to get the list with some of the elements filtered out, we can use a list comprehension
# rather than a normal for loop itself which can take up like 3 lines

array = [1,-1,-10,0,5,7,20,-100]

filtered = [n for n in array if n!=0]
print (filtered)

# one of the problems with this is that if the filtered list is too big, then the output wouldn't show 
# as it would prompt an error. To solve the error, print the filtered array in a for loop by iterating 
# through each element of the filtered array.


# something like  [n if n > 0 else 0 for n in mylist] is also possible