# By Eric Lee
# Class: CS 260
#1.-(40 points) Lists: two implementations, array and pointer (pages 41-46), operations: FIRST, END, RETRIEVE, LOCATE, NEXT, PREVIOUS, INSERT, DELETE, MAKENULL,



def FIRST(lst) :
    if lst.end is 0 :
        return -1
    else : 
        return 0

def END(lst) :
    return lst.end

def RETRIEVE(pos, lst) :
    if pos > lst.end :
        return None
    else :
        return lst.data[pos]

def LOCATE(x, lst) :
    for i in range(lst.end) :
        if lst.data[i] == x :
            return i

def NEXT(pos, lst) :
    if pos > lst.end or pos + 1 > lst.end:
        return None
    else :
        return pos + 1

def PREVIOUS(pos, lst) :
    if pos > lst.end or pos == 0 :
        return None
    else : 
        return pos - 1

def INSERT(x, pos, lst) :
    if pos > lst.end:
        return
    elif pos == lst.end :
        lst.data[pos] = x
    else :
        lst.data[pos+1:lst.end+1] = lst.data[pos:lst.end]
        lst.data[pos] = x
    lst.data = lst.data[:MAXNODES]
    lst.end += 1

def DELETE(pos, lst) :
    if pos == lst.end :
        lst.end -= 1
    else :
        lst.data[pos:lst.end-1] = lst.data[pos+1:lst.end]
        lst.end -= 1

class L : #List
	def __init__(self) :
		self.data = [None]*MAXNODES
		self.end = 0

def MAKENULL() :
    return L()


#---------------TEST LINE------------------------------------------------
def PRINTLIST(lst) :
	print lst.data[0:lst.end]
    
MAXNODES = 100
FIRST, END, RETRIEVE, LOCATE, NEXT, PREVIOUS, INSERT, DELETE, MAKENULL,
# Create an Empty List
mylist = MAKENULL()

# Insert Values into the list
for j in range(10) :
	INSERT(j, 0, mylist)
	
# Print the list
print "PRINTLIST: "
PRINTLIST(mylist)

# Insert new element at the end of the list
INSERT(99, END(mylist), mylist)
print "INSERT AT END OF LIST: "
PRINTLIST(mylist)

# Also uses the retrieve function
# Print the first element in the list
print "FIRST ELEMENT IN LIST (USING RETRIEVE): ", RETRIEVE(FIRST(mylist), mylist)

# Print the last element in the list
print "LAST ELEMENT (USING END): ", RETRIEVE(END(mylist), mylist)

# Print the element in position 7
print "ELEMENT 4's position (USING LOCATE): ", LOCATE(4, mylist)

# Print using next and previous
x = FIRST(mylist)
print "FIRST ELEMENT: ", RETRIEVE(x, mylist)
x = NEXT(x, mylist)
x = NEXT(x, mylist)
x = NEXT(x, mylist)
x = NEXT(x, mylist)
print "ELEMENT AT POSITION 6 (USING NEXT): ", RETRIEVE(x, mylist)
x = PREVIOUS(x, mylist)
print "ELEMENT AT POSITION 5 (USING PREVIOUS): ", RETRIEVE(x, mylist)

# Insert new element at position 5 of the list
INSERT(66, 5, mylist)
print "INSERT AT 5TH POS IN LIST: "
PRINTLIST(mylist)

# Delete the 2nd element in the list
DELETE(2, mylist)
print "DELETE 2ND POSITION IN LIST: " 
PRINTLIST(mylist)




