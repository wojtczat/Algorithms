""" 
Program to find LCA of n1 and n2 using one traversal of Binary tree
It handles all cases even when n1 or n2 is not there in tree
"""
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
 
# This function returns pointer to LCA of two given values n1 and n2 
# v1 is set as true by this function if n1 is found
# v2 is set as true by this function if n2 is found
def findLCAUtil(root, n1, n2, v):
     
    # Base Case
    if root is None:
        return None
 
    # IF either n1 or n2 matches ith root's key, report the presence by setting v1 or v2 
    # as true and return root (Note that if a key is ancestor of other, then the ancestor key becomes LCA)
    if root.key == n1:
        v[0] = True
        return root
    if root.key == n2:
        v[1] = True
        return root
 
    # Look for keys in left and right subtree
    leftLCA = findLCAUtil(root.left, n1, n2, v)
    rightLCA = findLCAUtil(root.right, n1, n2, v)
 
    # If both of the above calls return Non-NULL, then one key is present in once subtree 
    # and other is present in other, so this node is the LCA
    if leftLCA and rightLCA:
        return root 
 
    # Otherwise check if left subtree or right subtree is LCA
    return leftLCA if leftLCA is not None else rightLCA
 
 
def find(root, k):
     
    # Base Case
    if root is None:
        return False
     
    # If key is present at root, or if left subtree or right
    # subtree, return true
    if (root.key == k or find(root.left, k) or find(root.right, k)):
        return True
    return False
 
# This function returns LCA of n1 and n2 onlue if both
# n1 and n2 are present in tree, otherwise returns None
def findLCA(root, n1, n2):
     
    # Initialize n1 and n2 as not visited
    v = [False, False]
 
    # Find lac of n1 and n2 using the technique discussed above
    lca = findLCAUtil(root, n1, n2, v)
 
    # Returns LCA only if both n1 and n2 are present in tree
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and find(lca, n1)):
        return lca
 
    # Else return None
    return None
