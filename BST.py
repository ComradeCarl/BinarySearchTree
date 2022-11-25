'''
Author: Muhammad Momin Rahman
Date: 25th April 2022 
Last modified: 26th April 2022
Purpose: BST.py
'''

from bnode import BinaryNode
from pokemon import Pokemon

class BinaryTree:
    def __init__(self):
    #Constructor that creates a root defaulted to None
        self._root = None
    
    def rec_search(self, target, node):
    #A recursive search method which takes a target value and the node for match. It runs recursively if the node entry is not the target value.
        if node == None:
            return "\n No Pokemon was found. \n"
        else:
            if int(node.entry.get_id()) == target:
                return str(node.entry)
            elif int(node.entry.get_id()) < target:
                return self.rec_search(target, node.right)
            else:
                return self.rec_search(target, node.left)
    
    def insert(self, root, key):
    #An add/insert method that takes a root node and a key, which runs recursively if the root entry is equal to or less/greater than the key value.
        if root == None:
            return BinaryNode(key)
        else:
            if root.entry == key:
                raise RuntimeError("Duplicates are not allowed! \n")
            elif root.entry < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
            return root
     
    def remove(self, root, key):
    #Removal method to remove a root node given an integer key by the user.
        if root is None:
            return root
        elif root.entry.get_id() > key:
            root.left = self.remove(root.left, key)
            return root
        elif root.entry.get_id() < key:
            root.right = self.remove(root.right, key)
            return root
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left 
                root = None
                return temp
            else:
                _parent = root
                successor = root.right
                while successor.left != None:
                    _parent = successor
                    successor = successor.left
                if _parent != root:
                    _parent.left = successor.right
                else:
                    _parent.right = successor.right
                
                root.entry = successor.entry
                return root
        return root
    
    def minimum_node(self, root):
    #Method that returns the minimum node in order to assist the removal method.
        current = root
        while current.left != None:
            current = current.left
        return current
    
    def maximum_node(self, root):
    #Method that returns the maximum node. 
        current = root
        while current.right != None:
            current = current.right
        return current
     
    def copy(self, root):
    #Copy method to copy the root of a binary tree.
        if root is None:
            return None
        else:
            root_copy = BinaryNode(root.entry)
            root_copy.left = self.copy(root.left)
            root_copy.right = self.copy(root.right)
            return root_copy
    
    def pre_order(self, root):
    #Method that prints the left and right subtrees after the root has been visited (printed).
        if root:
            print(root.entry)
            self.pre_order(root.left)
            self.pre_order(root.right)
            
    def in_order(self, root):
    #Method that prints the left subtree, the root entry, then the right subtree recursively.
        if root:
            self.in_order(root.left)
            print(root.entry)
            self.in_order(root.right)
            
    def post_order(self, root):
    #Method that prints the left and right subtrees before the root has been visited. 
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.entry)
            
    