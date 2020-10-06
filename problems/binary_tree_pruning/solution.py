# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isLeafNode(root: TreeNode) -> TreeNode:
    return root.left is None and root.right is None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root.left is not None:
            if isLeafNode(root.left):
                if not root.left.val:
                    root.left = None
            else:
                root.left = self.pruneTree(root.left)

        if root.right is not None:
            if isLeafNode(root.right):
                if not root.right.val:
                    root.right = None
            else:
                root.right = self.pruneTree(root.right)
        
        if isLeafNode(root) and not root.val:
            return None

        return root