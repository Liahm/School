# By Eric Lee
# Class: CS 260
# Perform time measurements of the following five operations on lists: iterated insertion (in front, at the back), traversal, iterated deletion (in front, at the back). Run each of your procedures on three types of lists: a selected list type library data structure, your implementation of the list ADT with arrays, your implementation of the list ADT with pointers.

from timeit import Timer
#import from https://docs.python.org/2/library/timeit.html

#-------------------------------------LIST--------------------------------------------------
# Insert front
def insertLFront() :
	lst = [0]*n #define lst 
	for i in range(0, n) :
		lst.insert(0, 5)

# Insert back
def insertLBack() :
	lst = [0]*n
	for i in range(0, n) :
		lst.append(5)
	
# list traversal
def listLTraverse() :
	lst = [0]*n
	for i in range(len(lst)) :
		x = lst[i]

# Delete front
def deleteLFront() :
	lst = [0]*n
	for i in range(0, n) :
		del lst[0]

# Delete back
def deleteLBack() :
	lst = [0]*n
	for i in range(0, n) :
		del lst[-1]
#-------------------------------------LIST--------------------------------------------------



#----------------------------TESTING --------------------------------------------------
# control timer for assignment.  used to normalize timings that contain an assignment
def time() :
	lst = [0]*n

#-------------------------------------LIST--------------------------------------------------
EXEC = 1000
for i in range(1, 4) :	
	n = 10**i

	print "----- n = ", n, " -----"

	t = Timer("time()", "from __main__ import time")
	timeT = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	
	t = Timer("insertLFront()", "from __main__ import insertLFront")
	insfronttime = t.timeit(EXEC)/(EXEC*n) 
	print "Time per front List insertion: \t", insfronttime-timeT
	
	t = Timer("insertLBack()", "from __main__ import insertLBack")
	insbacktime = t.timeit(EXEC)/(EXEC*n) 
	print "Time per back List insertion: \t", insbacktime-timeT
	
	t = Timer("listLTraverse()", "from __main__ import listLTraverse")
	travtime = t.timeit(EXEC)/(EXEC*n) 
	print "Time per List traversal:      \t", travtime-timeT
	
	t = Timer("deleteLFront()", "from __main__ import deleteLFront")
	delfronttime = t.timeit(EXEC)/(EXEC*n) 
	print "Time per front List deletion: \t", delfronttime-timeT
	
	t = Timer("deleteLBack()", "from __main__ import deleteLBack")
	delbacktime = t.timeit(EXEC)/(EXEC*n) 
	print "Time per back List deletion: \t", delbacktime-timeT
	print

#-------------------------------------LIST--------------------------------------------------
print "----------------------------------------------------------"
print "----------------------------------------------------------"
print "----------------------------------------------------------"

#-------------------------------------ARRAY--------------------------------------------------
#Copied from arraylist.py
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

#----------------------------------------Array Timing------------------------------------------	
def insertAFront() :
	lst = MAKENULL()
	for i in range(0,n) :
		INSERT(5, 0, lst)
def insertABack() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(5, END(lst), lst)
def listATraverse() :
	lst = MAKENULL()
	for i in range(0,n) :
		INSERT(5, END(lst), lst)
	pos = FIRST(lst)
	while pos :
		pos=NEXT(pos,lst)
def deleteAFront() :
	lst = MAKENULL()
	for i in range(0,n) :
		INSERT(5, END(lst), lst)
	for i in range(0,n) :
		DELETE(0, lst)
def deleteABack() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(5, END(lst), lst)

	for i in range(0, n) :
		DELETE(END(lst), lst)
#-------------------------------------ARRAY----------------------------------------------------

#----------------------------TESTING --------------------------------------------------
# control timer for assignment.  used to normalize timings that contain an assignment
def time() :
	lst = [0]*n


#-------------------------------------ARRAY--------------------------------------------------
for i in range(1, 4) :
	n = 10**i
	MAXNODES = n

	print "----- n = ", n, " -----"

	t = Timer("time()", "from __main__ import time")
	timeT = t.timeit(EXEC)/(EXEC*n)

	t = Timer("insertAFront()", "from __main__ import insertAFront")
	insfronttime = t.timeit(EXEC)/(EXEC*n)
	print "Time per front Array insertion:", insfronttime-timeT

	t = Timer("insertABack()", "from __main__ import insertABack")
	insbacktime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per back Array insertion: \t", insbacktime-timeT
	
	t = Timer("listATraverse()", "from __main__ import listATraverse")
	travtime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per Array traversal:      \t", travtime-timeT
	
	t = Timer("deleteAFront()", "from __main__ import deleteAFront")
	delfronttime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per front Array deletion: \t", delfronttime-timeT
	
	t = Timer("deleteABack()", "from __main__ import deleteABack")
	delbacktime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per back Array deletion: \t", delbacktime-timeT

#-------------------------------------ARRAY--------------------------------------------------
print "----------------------------------------------------------"
print "----------------------------------------------------------"
print "----------------------------------------------------------"


#-------------------------------------POINTER--------------------------------------------------
#Copied from pointerlist.py

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

#----------------------------------------Pointer Timing------------------------------------------	
def insertPFront() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, 0, lst)
def insertPBack() :
	lst = MAKENULL()
	for i in range(0,n) :
		INSERT(i, END(lst), lst)
def listPTraverse() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, 0, lst)
	tmp = FIRST(lst)
	while tmp :
		tmp = NEXT(tmp)
def deletePFront() :
	lst = MAKENULL()
	for i in range(0,n) :
		INSERT(i, 0, lst)
	for i in range(0, n) :
		DELETE(0, lst)
def deletePBack() :
	lst = MAKENULL()
	for i in range(0, n) :
		INSERT(i, 0, lst)
	for i in range(0, n) :
		DELETE(END(lst), lst)
#-------------------------------------POINTER--------------------------------------------------



#----------------------------TESTING --------------------------------------------------
# control timer for assignment.  used to normalize timings that contain an assignment
def time() :
	lst = [0]*n


#-------------------------------------POINTER--------------------------------------------------
for i in range(1, 3) :
	n = 10**i
	MAXNODES = n

	print "----- n = ", n, " -----"

	t = Timer("time()", "from __main__ import time")
	timeT = t.timeit(EXEC)/(EXEC*n)

	t = Timer("insertPFront()", "from __main__ import insertPFront")
	insfronttime = t.timeit(EXEC)/(EXEC*n)
	print "Time per front Pointer insertion: \t", insfronttime-timeT

	t = Timer("insertPBack()", "from __main__ import insertPBack")
	insbacktime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per back Pointer insertion: \t", insbacktime-timeT
	
	t = Timer("listPTraverse()", "from __main__ import listPTraverse")
	travtime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per Pointer traversal:      \t", travtime-timeT
	
	t = Timer("deletePFront()", "from __main__ import deletePFront")
	delfronttime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per front Pointer deletion: \t", delfronttime-timeT
	
	t = Timer("deletePBack()", "from __main__ import deletePBack")
	delbacktime = t.timeit(EXEC)/(EXEC*n) # NUMREPS executions * n ops
	print "Time per back Pointer deletion: \t", delbacktime-timeT
#-------------------------------------POINTER--------------------------------------------------



