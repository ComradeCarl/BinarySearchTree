'''
Author: Muhammad Momin Rahman
Date: 25th April 2022 
Last modified: 26th April 2022
Purpose: bnode.py
'''

class BinaryNode:
    def __init__(self, entry):
    #Binary node constructor that takes in an entry and then creates three private members: entry, left, and right.
        self.entry = entry
        self.left = None 
        self.right = None 
        