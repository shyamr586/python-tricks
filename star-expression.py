# star expression is for unpacking a variable with arbitrary length.
# it works with any iterable data structure
# just '*' wont work so put something like *_ or *ign (ign=ignored) if the unpacked values are of no use

def getNItemsFromList(array):
    firstname, lastname, *contactdetails = array
    print ("\n")
    print ("The first name is: "+firstname)
    print ("The last name is: "+lastname)
    print ("Given contact details: "+str(contactdetails))
    print ("\n")


def getCharsFromString(text):
    firstchar, *middlechars, lastchar = text
    print ("The first char is: "+firstchar)
    print ("The middle chars is: "+str(middlechars))
    print ("The last char is: "+lastchar)

getNItemsFromList(["John", "Smith", "050-1231231", "04-1231231"])
getCharsFromString("Hello World!")