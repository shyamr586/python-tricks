# if you want to create a dictionary which has multiple values for a given key,
# we can make a normal dictionary in which a key connects to a list or set.
# But, making a list of values using normal dictionaries is a bit more complicated as we have to
# check if the key exists and then initialize a list and then give that list a value and finally
# connect that list to a key of the dict

# By using defaultdicct from collections module (same module as dequeue), we can:
# 1) add a value to a non existant key as it would create a key if it is non existant
# 2) make value a list/ set type easily

#the defaultdict can easily set new keys and add values to a key if they are a set or list, depending on what they
#are initialized as.

from collections import defaultdict

d = defaultdict(list)       #says that we need an object d with list as the vause for keys

print (d)
print (d["a"])

d["a"].append(1)
d["a"].append(2)
d["b"].append(1)

print (d)