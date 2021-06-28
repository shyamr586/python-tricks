
a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "a": 100,
    "y": 2,
    "x": 300
}

print (a.keys() & b.keys())         #print common keys of dicts
print (a.items() & b.items())       #print common key and value of the dicts

print (a.keys() - b.keys())         #print key in a and not in b
print (a.items() - b.items())       #print key and value that is in a and not in b