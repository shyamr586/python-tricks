#this is a famous leet code quesiton.

#in this, we have to find two elements from a list which sums upto a given number, called target.
#the challenge is we cannot have two loops as the time complexity will be too much.

#to make use of previous elements, we store the previous elements in a dictionary.
#Since the question asks to return the index of the values that sum up to the target, we store value:index in dict.

#one clever technique to find out if a pair exists in n turns is to check if the difference of the target and the
#current element exists in the dict.

#we cannot add the same element twice to get the target

def twoSum(nums,target):        #target is int and nums is list of ints

    myDict = {}
    for i in range(len(nums)):
        if (target-nums[i] in myDict):
            return [i,myDict[target-nums[i]]]
        else:
            myDict[nums[i]]=i

print(twoSum([1,2,3,4,5],9))
print(twoSum([6,3,4],10))
print(twoSum([8,6,4,3],14))
print(twoSum([2,3,9],11))