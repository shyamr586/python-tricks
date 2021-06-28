# sometimes the list comprehension would not be helpful because we have a complicated criteria to be 
# mentioned in the filter which would not fit in a line and might need a function. In those cases,
# use python's built in fiter() func.

array = [1,2,3,4,5,"%@$","!@#"]

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

filtered = list(filter(is_int,array))           #filter() creates an iterator so we need list()
print (filtered)