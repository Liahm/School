# By Eric Lee
# Class: CS 260
#4.-  (10 points) 2.3 b) Write a program to merge n sorted lists.

#Using pointers lists. Question doesn't tell us if we should use arraylist or pointerlist
#Copied from Assignment 1
#Classes
class L:
	def __init__(self):
		self.head = None
		self.cur = None
		
class N:
	def __init__(self):
		self.cargo = None
		self.nxt = None
	
	def __str__(self):
		return str(self.cargo) 

def FIRST(lst) :
    return lst.head
def END(lst) :
    if lst.head is None and lst.cur is None:
        return None
    else :
        tmp = lst.head
        while tmp.nxt:
            tmp = tmp.nxt
        return tmp
def RETRIEVE(pos, lst) :
    tmp = FIRST(lst)
    for i in range(0, pos) :
        if tmp.nxt != None :
            tmp = tmp.nxt
    return tmp.cargo
def LOCATE(x, lst) :
    count = 0
    tmp = FIRST(lst)
    while tmp :
        if tmp.cargo == x :
            return count
        else :
            count += 1
            tmp = tmp.nxt
    return -1
def NEXT(x) :
    return x.nxt
def PREVIOUS(x, lst) :
    tmp = FIRST(lst)
    while tmp :
        if(tmp.nxt == x) :
            return tmp
        else :
            tmp = tmp.nxt
    return None
def INSERT(x, pos, lst) :
    n = N()
    n.cargo = x
    if pos is None :
        n.nxt = None
        lst.head = n
        lst.cur = lst.head
        return
    elif(pos == FIRST(lst) and FIRST(lst) != END(lst)) or (pos == 0):
        n.nxt = lst.head
        lst.head = n
        lst.cur = lst.head
        return
    else :
        if lst.head is None :
            lst.head = n
            lst.cur = n
        else :
            tmp = FIRST(lst)
            while tmp and pos > 1 :
                tmp = tmp.nxt
                pos -= 1
            n.nxt = tmp.nxt
            tmp.nxt = n
        return
def DELETE(pos, lst) :
    tmp = FIRST(lst)
    if pos == 0 :
        lst.head = tmp.nxt
    elif pos == END(lst) :
        if tmp.nxt == None:
            lst = MAKENULL()
        else :
            while(tmp.nxt).nxt :
                tmp = tmp.nxt
            tmp.nxt = None
    else :
        while pos - 1 > 0 :
            tmp = tmp.nxt
            pos -= 1
        first = tmp
        second = tmp.nxt
        first.nxt = second.nxt
    lst.cur = lst.head
def MAKENULL() :
    tmp = L()
    return tmp

def PRINTLIST(lst) :
	tmp = FIRST(lst)
	if tmp is None :
		print "List is empty",
	else :
		while tmp :
			print tmp,
			tmp = tmp.nxt
	print

#-------------------------------"New" section-----------------------------------------------

def merge(list1, list2) :
    one = FIRST(list1)
    two = FIRST(list2)
    close = MAKENULL()

    while one and two : #Run as long as list1 and list2 are true
        if one.cargo <= two.cargo : 
            INSERT(one.cargo, END(close), close) #Add info from one to list
            one = NEXT(one)
        else : #two >= one
            INSERT(two.cargo, END(close), close) #Add info from two to list
            two = NEXT(two)

    #if one is longer
    if one is not None and two is None :
        while one :
            INSERT(one.cargo, END(close), close)
            one = NEXT(one)
    #elif two is longer
    elif two is not None and one is None :
        while two :
            INSERT(two.cargo, END(close), close)
            two = NEXT(two)
    
    return close

def mergen(*lst) :
    if len(lst) == 0 :
        return #list is empty
    elif len(lst) == 1 :
        return lst[0] #only 1 value
    else :
        tmp = merge(lst[0], lst[1]) #merge initial values
        for i in range(2, len(lst)) :
            tmp = merge(tmp, lst[i]) #merge up to length
        return tmp

#---------------TEST LINE------------------------------------------------
print("#---------------mergelists.py--------------------------------")
print("#---------------mergelists.py--------------------------------")
print("#---------------mergelists.py--------------------------------")

val1 = MAKENULL()
val2 = MAKENULL()
val3 = MAKENULL()
val4 = MAKENULL()
val5 = MAKENULL()

for i in range(1, 5, 1) :
    INSERT(i, END(val1), val1)
print "value 1: "
PRINTLIST(val1)

for i in range(0, 11, 2) :
    INSERT(i, END(val2), val2)
print "value 2: "
PRINTLIST(val2)

for i in range(7, 28, 7) :
    INSERT(i, END(val3), val3)
print "value 3: "
PRINTLIST(val3)

for i in range(3, 13, 3) :
    INSERT(i, END(val4), val4)
print "value 4: "
PRINTLIST(val4)

for i in range(4, 17, 4) :
    INSERT(i, END(val5), val5)
print "value 5: "
PRINTLIST(val5)

print " "
merged5 = mergen(val1, val2, val3, val4, val5)
merged4 = mergen(val1, val2, val3, val4)
merged3 = mergen(val1, val2, val3)
merged2 = mergen(val1, val2)
print "output of 5: "
PRINTLIST(merged5)
print "output of 4: "
PRINTLIST(merged4)
print "output of 3: "
PRINTLIST(merged3)
print "output of 2: "
PRINTLIST(merged2)
print "I have no idea what's going on"