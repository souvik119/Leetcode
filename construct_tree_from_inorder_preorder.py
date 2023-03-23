'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right


def build_tree(preorder, inorder):

    # if any of the list is empty then no tree
    if not preorder or not inorder:
        return None
    
    # in preorder list root is always the first one
    root = TreeNode(preorder[0])
    # get the index of root in inorder list so we can divide that into left and right subtrees
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root

