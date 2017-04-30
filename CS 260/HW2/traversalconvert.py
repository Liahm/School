# By Eric Lee
# Class: CS 260
# 7.-(15 points) 3.13 Let T be a tree in which every nonleaf node has two children. Write a program to convert
                        #a. a preorder listing of T into a postorder listing,
                        #b. a postorder listing of T into a preorder listing,
                        #c. a preorder listing of T into an inorder listing.

def pretopost(lst) :
    if len(lst) == 3 : 
        tmp = lst[:]
        tmp[0:2] = lst[1:3]
        tmp[2] = lst[0]
        return tmp
    else :
        tmp = lst
        tmp = pretopost(lst[1:((len(lst)+1)/2)]) + pretopost(lst[((len(lst)+1)/2):]) + [lst[0]] 
        #list from start to the current length of the list divided by the children 
        return tmp

def postopre(lst) :
    if len(lst) == 3 :
        tmp = lst[:]
        tmp[1:3] = lst[0:2]
        tmp[0] = lst[2]
        return tmp
    else :
        tmp = [lst[-1]] + postopre( lst[ 0 : ( (len(lst)-1) /2) ] ) + postopre( lst[ ( (len(lst)-1) /2) : -1 ] )
        #Last item + current first item in the list till the last children + the last children to the last item
        return tmp

def pretoin(lst) :
    if len(lst) == 3 :
        tmp = lst[:]
        tmp[1:3] = lst[0:2]
        tmp[0] = lst[2]
        return tmp
    else :
        tmp = lst
        tmp = pretoin( lst[ 1 : ( (len(lst)+1) /2) ] ) + [lst[0]] + pretoin( lst[ ((len(lst)+1) /2) : ] )
        #list from first to the sum of the next children plus current item plus the next children and copy.
        return tmp


#---------------TEST LINE------------------------------------------------
print("#---------------traversalconvert.py--------------------------------")
print("#---------------traversalconvert.py--------------------------------")
print("#---------------traversalconvert.py--------------------------------")                 

pre = ['A', 'B', 'D', 'H', 'I', 'E', 'J', 'K', 'C', 'F', 'L', 'M', 'G', 'N', 'O']
print "Data = 'A', 'B', 'D', 'H', 'I', 'E', 'J', 'K', 'C', 'F', 'L', 'M', 'G', 'N', 'O'"
print " "
#Order of left most children
print "pre to post: "
post = pretopost(pre)
print post

pre2 = postopre(post)
print "post to pre: "
print pre2

ordered = pretoin(pre)
print "pre to in: "
print ordered

