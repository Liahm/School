# By Eric Lee
# Class: CS 260
# Pointers section for question 2 - TOP, POP, PUSH, EMPTY, MAKENULL,

class S :
    def __init__(self) :
        data = None
        end = None
        return

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
	tmp = S()
	tmp.data = [0]*MAXLENGTH
	tmp.end = 0
	return tmp

#------------TEST-----------------------------

def PRINTSTACK(stack) :
	print stack.data[:stack.end]
	return

MAXLENGTH = 100

#Clear
mystack = MAKENULL()

#Add 10
for i in range(10) :
    PUSH(i, mystack)

#print it
print "Stack info: "
PRINTSTACK(mystack)

#TOP
print "Top is: "
TOP(mystack)
PRINTSTACK(mystack)

#POP
print "Pop: "
POP(mystack)
PRINTSTACK(mystack)

#PUSH
PUSH(15, mystack)
PRINTSTACK(mystack)

#EMPTY
print "Empty?: ", EMPTY(mystack)

#empty the stack
mystack = MAKENULL()
print "Stack is now empty: ", EMPTY(mystack)
