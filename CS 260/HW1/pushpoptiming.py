#--------------------------------------Push and Pop--------------------------------------------
from timeit import Timer
#----------STACK---------------------------------
def insertionPush() :
        lst = [0]*n
        for i in range(0, n) :
                lst.append(5)

def deletionPop() :
        lst= [0]*n
        for i in range(0, n) :
                del lst[-1]
#----------STACK-------------------------

def time () :
        lst = [0]*n

#----------STACK-------------------------
EXEC = 1000
for i in range(1,4) :
        n= 10**i

        print "n = ", n

        t = Timer("time()", "from __main__ import time")
        timeT = t.timeit(EXEC)/(EXEC*n)

        t = Timer("insertionPush()", "from __main__ import insertionPush")
        insbacktime = t.timeit(EXEC)/(EXEC*n)
        print "Time per Push Stack insertion: \t", insbacktime-timeT

        t = Timer("deletionPop()", "from __main__ import deletionPop")
        delbacktime = t.timeit(EXEC)/(EXEC*n)
        print "Time per back Stack deletion: \t", delbacktime-timeT
        print

print "----------------------------------------------------------"
print "----------------------------------------------------------"
print "----------------------------------------------------------"
#----------ARRAY-----------------------------
class S :
    def __init__(self) :
        self.container = []
        self.head = None
        self.cur = None
        data = None
        end = None
        return None

def TOP(stack) :
    return stack.data[0]

def POP(stack) :
        stack.end -= 1
        return

def PUSH(pos, stack) :
    stack.data[stack.end] = pos
    stack.end += 1
    return

def EMPTY(stack) :
        if stack.end == 0 :
                return True
        else :
                return False
def MAKENULL() :
        MAXLENGTH = 100
        tmp = S()
        tmp.data = [0]*MAXLENGTH
        tmp.end = 0
        return tmp

def insertSBack() :
        lst = MAKENULL()
        for i in range(0, n) :
                lst.container.append(i)

def deleteSBack() :
        lst = MAKENULL()
        for i in range(0, n) :
                PUSH(i, lst)
        for i in range(0, n) :
                POP(lst)


def time() :
        lst = [0]*n

#-----------------------STACK----------------------------------
for i in range(1,3) :
        n = 10**i
        MAXNODE = n

        print "n = ", n

        t = Timer("time()", "from __main__ import time")
        timeT = t.timeit(EXEC)/(EXEC*n)

        t = Timer("insertSBack()", "from __main__ import insertSBack")
        insbacktime = t.timeit(EXEC)/(EXEC*n)
        print "Time per back Stack insertion: \t", insbacktime-timeT

        t = Timer("deleteSBack()", "from __main__ import deleteSBack")
        delbacktime = t.timeit(EXEC)/(EXEC*n)
        print "Time per back Stack deletion: \t", delbacktime-timeT

print "----------------------------------------------------------"
print "----------------------------------------------------------"
print "----------------------------------------------------------"
#-----------------------POINTER----------------------

class S:
        def __init__(self):
                self.top = None

class N:
        def __init__(self):
                self.cargo = None
                self.nxt = None

        def __str__(self):
                return str(self.cargo)

def TOP(lst) :
    return lst.top

def POP(lst) :
    lst.top = lst.top.nxt
    return
def PUSH(x, lst) :
    top = N()
    top.cargo = x
    top.nxt = lst.top
    lst.top = top
    return

def EMPTY(lst) :
    if lst.top is None:
        return True
    else :
        return False

def MAKENULL() :
    tmp = S()
    return tmp

def insertPBack() :
        lst = MAKENULL()
        for i in range(0, n) :
                PUSH(i, lst)

def deletePBack() :
        lst = MAKENULL()
        for i in range(0, n) :
                PUSH(i, lst)
        for i in range(0, n) :
                POP(lst)

#------------------------POINTER-----------------------

def time() :
        lst = [0]*n

#--------------------------POINTER--------------------
for i in range(1,3) :
        n = 10**i


        print "n = ", n

        t = Timer("time()", "from __main__ import time")
        timeT = t.timeit(EXEC)/(EXEC*n)

        t = Timer("insertPBack()", "from __main__ import insertPBack")
        insbacktime = t.timeit(EXEC)/(EXEC*n)
        print "Time per back Pointer insertion: \t", insbacktime-timeT


        t = Timer("deletePBack()", "from __main__ import deletePBack")
        delbacktime = t.timeit(EXEC)/(EXEC*n)
        print "Time per back Pointer deletion: \t", delbacktime-timeT