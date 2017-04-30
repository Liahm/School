# By Eric Lee
# Class: CS 260
#2.4 Write a program to concatenate a list of lists

#Using pointers lists. Question doesn't tell us if we should use arraylist or pointerlist
#Copied from Assignment 1

class L:
	def __init__(self):
		self.head = None
		self.cur = None
		self.nextlist = None #Added this line

		
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

class S : #S variable for list of lists... couldn't stay focused with a variable called LoL
    def __init__(self) :
        self.head = None
        self.pos = None

def MakeS() :
    return S()

def AppendToS(lst, s):
    if s.head is None :
        s.head = lst
        s.pos = lst
        lst.nextlist = None
    else :
        tmp = s.head #tmp is list head
        while tmp.nextlist : #concatenate the list of lists
            tmp = tmp.nextlist
        tmp.nextlist = lst
    return

def concatenate(s):
    close = MAKENULL()
    x = s.head
    while x :
        listx = x.head
        while listx :
            INSERT(listx.cargo, END(close), close)
            listx = listx.nxt
        x = x.nextlist
    return close

def printS(s) :
    x = s.head
    while x :
        listx = x.head
        while listx :
            print listx,
            listx = listx.nxt
        x = x.nextlist
        if x is None :
            print " "
        else :
            print "End"
    return

#---------------TEST LINE------------------------------------------------
print("#---------------listconcat.py--------------------------------")
print("#---------------listconcat.py--------------------------------")
print("#---------------listconcat.py--------------------------------")

val1 = MakeS()
val2 = MAKENULL()
val3 = MAKENULL()

for i in range(0, 11, 2) :
    INSERT(i, END(val2), val2)
    INSERT(i+1, END(val3), val3)
print "list 2 or val2 or evens"
PRINTLIST(val2)
print "list 3 or val3 or odds"
PRINTLIST(val3)

print "appending val2 to val1..."
AppendToS(val2, val1)
print "Appended: "
printS(val1)

print "appending val2 to val1..."
AppendToS(val3, val1)
print "Appended: "
printS(val1)

print " "
print "concatenating"
x = MAKENULL()
x = concatenate(val1)
print "val1: "
PRINTLIST(x)
