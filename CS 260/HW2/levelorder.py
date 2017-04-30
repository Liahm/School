# By Eric Lee
# Class: CS 260
# 6.-(20 points) 3.10 The level-order listing of the nodes of a tree first lists the root, then all nodes of depth 1, then all nodes of depth 2, and so on. Nodes at the same
# depth are listed in left-to-right order. Write a program to list the nodes of a tree in level-order

#Using the queues, as the hint says. It also "Forced" me to do #1
#-------------------------Queue---------------------------------------------------
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

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#--------------------------Trees--------------------------------------------------
#Chapter 3.2
class node :
    def __init__(self) :
        self.label = None
        self.lc = None #left child
        self.rs = None #right sibling (I wonder why the book says right sibling and not right child)
        self.parent = None

    def __str__(self) :
        return str(self.label)

class tree :
    def __init__(self) :
        self.cellspace = None
        self.root = None

def MAKENULL() :
    tmp = tree()
    tmp.cellspace = [None]*MAXNODES
    return tmp

def PARENT(n, T) :
    return T.cellspace[n.parent] #return tree's n cellspace, or the top

def LEFTMOST_CHILD(n, T) :
    if n.lc is None : #check if left child exist
        return None

def RIGHT_SIBLING(n, T):
	if n.rs is None : #check if right sibling exist
		return None
	else :
		return T.cellspace[n.rs]
	print n, "Doesn't exist"

def LABEL(n) :
    return n.label

def CREATE0(v) : #Create height 0
	tmp = MAKENULL()
	#set root's values
	tmp.cellspace[v] = node()
	tmp.cellspace[v].label = v
	
	# root is v
	tmp.root = v
	return tmp

def CREATE1(v, T) : #Height 1
	tmp = MAKENULL()

	for i in range(0, MAXNODES) :
		if T.cellspace[i] is not None :
			tmp.cellspace[i] = T.cellspace[i]

	tmp.cellspace[v] = node()
	tmp.cellspace[T.root] = node()

    # set root's values
	tmp.cellspace[v].label = v
	tmp.cellspace[v].lc = T.root
	tmp.cellspace[v].rs = None	# Copy paste format
	
	# set T's values
	tmp.cellspace[T.root] = T.cellspace[T.root]
	tmp.cellspace[T.root].rs = None
	tmp.cellspace[T.root].parent = v

	tmp.root = v
	return tmp

def CREATE2(v, T1, T2) : #Height 2
    #Uhm, to create more do we have to continue expanding this?
    #Not sure how a loop would do this because the argument inputs change everytime, as in there are more.
    #Array arguments?

    tmp = MAKENULL()

    for i in range(0, MAXNODES) :
        if T1.cellspace[i] is not None :
            tmp.cellspace[i] = T1.cellspace[i]
        elif T2.cellspace[i] is not None :
            tmp.cellspace[i] = T2.cellspace[i]
    
    #First root
    tmp.cellspace[v] = node()
    tmp.cellspace[T1.root] = node()
    tmp.cellspace[T2.root] = node()

    #New root, this will continue on
    tmp.cellspace[v].label = v
    tmp.cellspace[v].lc = T1.root #no right sibling

    tmp.cellspace[T1.root] = T1.cellspace[T1.root]
    tmp.cellspace[T1.root].rs = T2.root
    tmp.cellspace[T1.root].parent = v

    tmp.cellspace[T2.root] = T2.cellspace[T2.root]
    tmp.cellspace[T2.root].rs = None
    tmp.cellspace[T2.root].parent = v

    tmp.root = v
    return v    
    
    #Not sure if I should do more, but I am tired of copy/paste/change data and see if it's correct

def ROOT(T) :
    return T.cellspace[T.root]

def printTree(n, T) :
    if n.lc is None :
        print n,
    else :
        printTree(T.cellspace[n.lc], T)
        print n,
        tmp = LEFTMOST_CHILD(n, T)
        tmp = RIGHT_SIBLING(tmp, T)
        while tmp is not None :
            printTree(tmp, T)
            tmp = RIGHT_SIBLING(tmp, T)

#---------------TEST LINE------------------------------------------------
print("#---------------levelorder.py--------------------------------")
print("#---------------levelorder.py--------------------------------")
print("#---------------levelorder.py--------------------------------")
    

def makeHeight(n, T, Qu, i) : #nodes, trees, queue, var
	if LEFTMOST_CHILD(n, T) is None :
		if Qu[i] is None :
			Qu[i] = Q() #I should had named it something else, OH WELL
		ENQUEUE(n.label, Qu[i])
	else:
		tmp = LEFTMOST_CHILD(n, T)
		while tmp is not None :
			makeHeight(tmp, T, Qu, i+1)
			tmp = RIGHT_SIBLING(tmp, T)
		if Qu[i] is None :
			Qu[i] = Q()
		ENQUEUE(n.label, Qu[i])

MAXNODES = 100

A = CREATE0(2)
B = CREATE0(4)
C = CREATE2(6, A, B)

D = CREATE0(6) 
E = CREATE1(7, D)


x = [None]*MAXNODES 
makeHeight(ROOT(E), E, x, 0)

for i in range(MAXNODES) :
    if x[i] is not None :
        print "maxheight should be 7"
        printQueue(x[i])
