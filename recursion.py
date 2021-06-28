# recursion is for breaking down a relatively larger problem to smaller parts.
# it is considered when the thing you are working on has too many branches
# and acts a substitute to the normat iterations(for and while).
# some languages dont even have loops, in which recursions are used.

def factorial(number):
    if (number==0):                                 # this is called base case, a condition that stops the program to run infinitely
        return 1
    else:                                           # and this is the recursion case which ofc has the recursion 
        return (number*factorial(number-1))         #(calling a func in a func in simple words)
                                        
print (factorial(4))