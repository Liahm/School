# By Eric Lee
# Class: CS 260
# 1.=(10 points) Queues: one implementation, pointer (pages 57-60), operations: FRONT, ENQUEUE, DEQUEUE, EMPTY, MAKENULL,

class N:
	def __init__(self):
		self.cargo = None
		self.nxt = None
	
	def __str__(self):
		return str(self.cargo) 

class Q :
    def __init__(self):
        self.front = None
        self.cur = None

def FRONT(q):
    return q.front

def ENQUEUE(x, q):
    tail = N()
    tail.cargo = x
    tail.nxt = None

    if EMPTY(q) :
        q.front = tail
        q.cur = tail
    else :
        tmp = q.front
        while tmp.nxt :
            tmp = tmp.nxt
        tmp.nxt = tail
        q=tmp

    return

def DEQUEUE(q):
    q.front = q.front.nxt #delete current front
    q.cur = q.front

    return
def EMPTY(q):
    if q.front is None :
        return True
    else :
        return False

def MAKENULL():
    tmp = Q()
    front = N()
    cur = front

    return tmp

def printQueue(q) :
        tmp = FRONT(q)
        if tmp is None :
                print "Queue is empty",
        else :
                while tmp :
                        print tmp,
                        tmp = tmp.nxt
        print
#---------------TEST LINE------------------------------------------------
print("#---------------listconcat.py--------------------------------")
print("#---------------listconcat.py--------------------------------")
print("#---------------listconcat.py--------------------------------")

mylist = MAKENULL()

for i in range(10) :
    ENQUEUE(i, mylist)

#ENQUEUE
print "Enqueue: "
printQueue(mylist)
print " "

#front
print "Front: "
x = FRONT(mylist)
print x
print " "

#Dequeue
print "Dequeue: "
x = DEQUEUE(mylist)
printQueue(mylist)
print " "

#empty
print "False Empty: "
EMPTY(mylist)
printQueue(mylist)
print " "

print "True Empty: "
mylist = MAKENULL()
EMPTY(mylist)
printQueue(mylist)