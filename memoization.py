#memoization is basically caching things.
#memoiztion can be used in combination with recursion so that when there is more recursions occuring, we can
#rely on the data to be saved in the cache.
#we can make a list for the items, where the list acts like a cache file and the recurring items are saved in the 
#list.
#but, luckily there is also a built in python method for this.

from functools import lru_cache

@lru_cache()
def fib(pos):                           #searching for a position in the 1000's takes a long time, compared to
                                        #using memoization techniques, which coputes faster.
    if (pos==0 or pos==1):
        return pos                      #the first position, 0 has value 0 and same for second (1)
    elif (pos==2):
        return 2
    else:
        return fib(pos-1)+fib(pos-2)    #like i said, sum of last two terms
    
position = input("Enter the number of positions in the sequence you want to see: ")
position = int(position)
# print(fib(position))          #use this if you dont want sequence and only value of that position
for i in range(1,position+1):
    print(i,":",fib(i))
