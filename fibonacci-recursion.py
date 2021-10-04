#a fibonacci series is a sequence of number which starts with 0 and 1 and sums the previous two numbers to 
#create a new number, which goes infinitely.
#interesting note: the ratio of the numbers is the golden ratio (wow cool).

#this fibonacci series is done using recursion to make code look cleaner.

def fib(pos):
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