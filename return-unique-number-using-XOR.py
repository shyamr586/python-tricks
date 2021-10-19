#this is from a leetcode solution to a problem where we have to return the only unique number in a list.
#the problem states that if the length of the array is 1 then return the element or else, if 
#the list is [1,2,2,1,3] return 3.

# IT IS SAID THAT ELEMENTS THAT ARE NOT UNIQUE APPEARS EXACTLY TWICE.

#other examples: [4,3,2,1,2,3,1] should return 4
#[2,2,1] should return 1

#to remove all duplicate values, (we know all occurs twice except one is unique), we use XOR.
#XOR is exclusive or, which can be used using ^. 

#Example of using XOR: 
#if we are considering booleans, true can be treated as 1 and false can be treated as 0.

# true^false will give true
# true^true will give false
# false^false will give false
# this is because XOR literally tries to exclude duplicates.

# In numbers, this can be a bit complicated because if we take, say, 19^21, we get 6... to make things short
# it checks the bits of 19 and 21 and returns the exclusive bits, which gives 6.

#For this problem, XOR is the best solution because if two numbers occur, their XOR becomes 0.
#example: A^A^B = 0^B (0 becase A^A = 0) = B
#wxample2: A^A^B^B^C = 0^0^C = C

arr = [1,1,2,3,2,3,4]
answer = 0
for i in range(len(arr)):
    answer^=arr[i]
print (answer)

#big explanation because this is the first time i have ever seen a XOR....