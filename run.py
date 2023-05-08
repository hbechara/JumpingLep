# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:32:21 2023

@author: Hannah
"""
import random
from Tree import AVLTree

tree = AVLTree()


def create_leprechauns(n, tree):
    for i in range(1, n+1):
        gold = 1000000
        place = 1000000 * random.uniform(-1,1)
        tree.insert(place, gold)
 
def simulate_iteration(tree):
    # Create an array with the in-order keys
    node = tree.root
    vals = []
    vals = tree.inorder(tree.root, vals)
    #print(vals)
  
    
    
    for node in vals:
        
        new_place = node.key + random.uniform(-1,1) * node.value
        print("leprechaun", node.key, " jumps to ", new_place)
        # Delete the leprechaun from the tree with its old place as the key
        tree.delete(tree.root, node.key)
        # Insert the leprechaun into the tree with its new place as the key and its old gold value as the value
        tree.insert(new_place, node.value)
       
        # Find the predecessor and successor of the leprechaun in the tree, which are the nearest leprechauns on either side of it on the horizon
        pred = tree.find_predecessor(new_place)
       
        succ = tree.find_successor(new_place)
        
        
        # If there is a predecessor, steal half of its gold and add it to the leprechaun's gold value
        if pred is not None:
           print("leprechaun steals", pred.value / 2)
           node.value += pred.value / 2
           pred.value /= 2
        else: print("Nothing to steal")
        # If there is a successor, steal half of its gold and add it to the leprechaun's gold value
        if succ is not None:
           print("leprechaun steals", succ.value / 2)
           node.value += succ.value / 2
           succ.value /= 2
        else: print("Nothing to steal")
        # Set the next leprechaun to be processed by finding the successor of the current leprechaun in the tree
        

# A utility function to print the key-value pairs of a subtree in order
def print_inorder(node):
    if node is not None:
        print_inorder(node.left) # Print left subtree recursively
        print("Place:", node.key, "Gold:", node.value) # Print key-value pair of node
        print_inorder(node.right) # Print right subtree recursively        

# Define a function that runs the simulation for a given number of iterations and prints the final gold values of each leprechaun
def run_simulation(n, iterations):
    # Create n leprechauns with initial gold values and places them on the horizon using the AVL tree
    tree = AVLTree()
    print("Creating", n, "leprechauns. This is the tree at the start")
    create_leprechauns(n, tree)
    
    print_inorder(tree.root)
    # Loop for iterations times
    for i in range(iterations):
        # Simulate one iteration of the simulation by processing each leprechaun in order and updating their gold values and positions
        print("simulating jump...")
        simulate_iteration(tree)
        #print_inorder(tree.root)
    # Print the final gold values of each leprechaun by traversing the tree in order
    print("The final gold values of each leprechaun are:")
    print_inorder(tree.root)     
    

run_simulation(5, 1)
