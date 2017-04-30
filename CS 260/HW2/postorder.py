# By Eric Lee
# Class: CS 260
# 8.-(15 points) 3.14 Write a program to evaluate
            #b. postorder
            #arithmetic expressions

#Copied from problem 7

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
        #list from first to the sum of the next children plus current item plus the next children and everything else.
        return tmp


def calculatepost(lst) :
    if len(lst) == 3 :
        if lst[-1] == '+' :
            return lst[0] + lst[1]
        elif lst[-1] == '-' :
            return lst[0] - lst[1]
        elif lst[-1] == '*' :
            return lst[0] * lst[1]
        elif lst[-1] == '/' :
            return lst[0] / lst[1]
        elif lst[-1] == '%' :
            return lst[0] % lst[1]
    else :
        if lst[-1] == '+' :
            return calculatepost(lst[: ((len(lst)-1)/2)]) + calculatepost(lst [ ((len(lst) - 1)/2) : -1])
                #list from start to the end children plus the children to the last item
        elif lst[-1] == '-' :
            return calculatepost(lst[: ((len(lst)-1)/2)]) - calculatepost(lst [ ((len(lst) - 1)/2) : -1]) 
            #same as above but minus
        elif lst[-1] == '*' :
            return calculatepost(lst[: ((len(lst)-1)/2)]) * calculatepost(lst [ ((len(lst) - 1)/2) : -1]) 
            #same as above but multiplicative
        elif lst[-1] == '/' :
            return calculatepost(lst[: ((len(lst)-1)/2)]) / calculatepost(lst [ ((len(lst) - 1)/2) : -1]) 
            #same as above but dividing
        elif lst[-1] == '%' :
            return calculatepost(lst[: ((len(lst)-1)/2)]) % calculatepost(lst [ ((len(lst) - 1)/2) : -1]) 
            #same as above but mod


#----------------------------------Testing------------------------------------
print("#---------------------------postorder.py--------------------------------")
print("#---------------------------postorder.py--------------------------------")
print("#---------------------------postorder.py--------------------------------")  

print "Calculating post 1: "
post = [4, 6, '+', 20, 10, '+', '*']
print post
print calculatepost(post)

print "Calculating post 2: "
post = [24, 25, '*', 20, 10, '+', '/']
print post
print calculatepost(post)

print "Calculating post 3: "
post = [14, 26, '+', 40, 17, '+', '%']
print post
print calculatepost(post)