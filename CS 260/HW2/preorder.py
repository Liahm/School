# By Eric Lee
# Class: CS 260
# 8.-(15 points) 3.14 Write a program to evaluate
            #a. preorder
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



def calculatepre(lst) :
    if len(lst) == 3 :
        if lst[0] == '+' :
            return lst[1] + lst[2]
        elif lst[0] == '-' :
            return lst[1] - lst[2]
        elif lst[0] == '*' :
            return lst[1] * lst[2]
        elif lst[0] == '/' :
            return lst[1] / lst[2]
        elif lst[0] == '%' :
            return lst[1] % lst[2]
    else :
        if lst[0] == '+' :
            return calculatepre(lst[1 : ((len(lst)+1)/2)]) + calculatepre(lst [ ((len(lst) + 1)/2) :])
                #list from 1 to the end+1 children plus the children to the END
        elif lst[0] == '-' :
            return calculatepre(lst[1 : ((len(lst)+1)/2)]) - calculatepre(lst [ ((len(lst) + 1)/2) :]) 
            #same as above but minus
        elif lst[0] == '*' :
            return calculatepre(lst[1 : ((len(lst)+1)/2)]) * calculatepre(lst [ ((len(lst) + 1)/2) :]) 
            #same as above but multiplicative
        elif lst[0] == '/' :
            return calculatepre(lst[1 : ((len(lst)+1)/2)]) / calculatepre(lst [ ((len(lst) + 1)/2) :]) 
            #same as above but dividing
        elif lst[0] == '%' :
            return calculatepre(lst[1 : ((len(lst)+1)/2)]) % calculatepre(lst [ ((len(lst) + 1)/2) :]) 
            #same as above but mod


#----------------------------------Testing------------------------------------
print("#---------------------------preorder.py--------------------------------")
print("#---------------------------preorder.py--------------------------------")
print("#---------------------------preorder.py--------------------------------")



print "Calculating pre 1: "
pre = ['*', '+', 10, 20, '+', 6, 4]
print pre
print calculatepre(pre)

print "Calculating pre 2: "
pre = ['+', '-', 40, 14, '*', 4, 9]
print pre
print calculatepre(pre)

print "Calculating pre 3: "
pre = ['-', '%', 5, 20, '/', 2, 7]
print pre
print calculatepre(pre)

print "Tried to make them bigger, but had issues"
