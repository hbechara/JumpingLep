# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:33:40 2023

@author: Hannah
"""
from Tree import AVLTree


tree = AVLTree()

tree.insert(50, 20)
tree.insert(40, 20)
tree.insert(60, 20)
tree.insert(70, 20)
tree.insert(80, 20)
print(tree.root.key)

print(tree.find_max(tree.root).key)
print(tree.find_min(tree.root).key)

print(tree.find_successor(50).key)
print(tree.find_predecessor(50).key)

print(tree.find_successor(70).key)
print(tree.find_predecessor(70).key)

vals = []
print(tree.inorder(tree.root, vals))

tree.delete(tree.root, 80)

vals = []
print(tree.inorder(tree.root, vals))