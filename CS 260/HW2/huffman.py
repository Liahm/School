# By Eric Lee
# Class: CS 260
#(30 points) Huffman algorithm (3.4). For a given collection of characters and probabilities your program should create the Huffman tree and print out the codes for all the characters. Test your implementation on data provided in problem 3.20.

import sys
import re
from heapq import heapify, heappop, heappush
#Utilizing heapq because of various hours of thinking I couldn't make it work

def huffman(t, code_str = ''):

# Recursive call the tree branches
        if len(t) < 3:
                print('%s: %s' % (t[1], code_str))
        else:
                huffman(t[1], code_str + '0')
                huffman(t[2], code_str + '1')

# Test tree from exercise 3.20 from the book
tree = [
        [0.07, 'a'],
        [0.09, 'b'],
        [0.12, 'c'],
        [0.22, 'd'],
        [0.23, 'e'],
        [0.27, 'f']
]

# Convert the input into a binary tree
heapify(tree)

# Sort the tree into a Huffman tree.
while len(tree) > 1:
        x = heappop(tree)
        y = heappop(tree)
        total_prob = x[0] + y[0]
        heappush(tree, (total_prob, x, y))

#--------------------------Testing--------------------------
print "---------------------HUFFMAN-----------------------"
print "---------------------HUFFMAN-----------------------"
print "---------------------HUFFMAN-----------------------"
huffman(tree[0])