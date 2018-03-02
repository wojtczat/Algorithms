class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def findLCAUtil(root, n1, n2, v):
    if root is None:
        return None
    if root.key == n1:
        v[0] = True
        return root
    if root.key == n2:
        v[1] = True
        return root
    leftLCA = findLCAUtil(root.left, n1, n2, v)
    rightLCA = findLCAUtil(root.right, n1, n2, v)
    if leftLCA and rightLCA:
        return root
    return leftLCA if leftLCA is not None else rightLCA


def find(root, k):
    if root is None:
        return False
    if (root.key == k or find(root.left, k) or find(root.right, k)):
        return True
    return False

def findLCA(root, n1, n2):
    v = [False, False]
    lca = findLCAUtil(root, n1, n2, v)

    if v[0] and v[1] or v[0] and find(lca, n2) or v[1] and find(lca, n1):
        return lca
    return None
