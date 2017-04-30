# By Eric Lee
# Class: CS 260
# Pointers section for question 1

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

#--------------------TEST----------------------
def PRINTLIST(lst) :
	tmp = FIRST(lst)
	if tmp is None :
		print "List is empty",
	else :
		while tmp :
			print tmp,
			tmp = tmp.nxt
	print
#MAKENULL
mylist = MAKENULL()
#Create data
for i in range(10) :
    INSERT(i, 0, mylist)
#print data
print "Printlist: "
PRINTLIST(mylist)

#print first
print "Print first pos: "
x = FIRST(mylist)
print x

#print END
print "Print end: "
x = END(mylist)
print x

#print RETRIEVE
print "Retrieve value at pos 2"
print RETRIEVE(2, mylist)
#print LOCATE
print "Locate Pos 6"
print LOCATE(6, mylist)
#print next
print "NEXT! You know, the show? Nope? okay... next: "
x = FIRST(mylist)
print x
#print PREVIOUS
print "beep... beep..beep- previous: "
x = PREVIOUS(x, mylist)
print x
#print Insert
INSERT(20, 2, mylist)
print "Insert at second position in list: "
PRINTLIST(mylist)
#print DELETE
DELETE(END(mylist), mylist)
print "Delete the end: "
PRINTLIST(mylist)