# By Eric Lee
# Class: CS 260
# 2.- (20 points) Stacks: two implementations, array and pointer (pages 53-56), operations: TOP, POP, PUSH, EMPTY, MAKENULL,

#Classes
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

#Testing

def PRINTSTACK(lst) :
    tmp = TOP(lst)
    if tmp is None :
        print "(Stack is empty)",
    else : 
        while tmp :
            print tmp,
            tmp = tmp.nxt
    print

mystack = MAKENULL()

#Push
print "Creating stack"
for i in range(1,10) :
    PUSH(i, mystack)
PRINTSTACK(mystack)

#Pop
print "Pop x amount of elements"
POP(mystack)
POP(mystack)
POP(mystack)
PRINTSTACK(mystack)

#Empty stack?
print "Stack is empty?: ", EMPTY(mystack)

#Empty the stack and test if True
mystack = MAKENULL()
PRINTSTACK(mystack)
print "Stack is now empty", EMPTY(mystack)