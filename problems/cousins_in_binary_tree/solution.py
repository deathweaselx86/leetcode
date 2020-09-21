# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def get_depth(node: TreeNode, parent: TreeNode, value: int, current_depth:int):
        depth = -1
        my_parent = parent
        
        # return -1 and parent node if this isn't actually a node
        if not node:
            return (depth, parent)
        
    
        # return depth and given parent node if this is the node we're looking for
        if node.val == value:
            return (current_depth, parent)

        # for left and right, get depth of child nodes
        for n in (node.left, node.right):
            if n:
                # we call this my_parent because it may not be the same as parent here
                depth, my_parent = Solution.get_depth(n, node, value, current_depth=current_depth + 1)
            if depth > -1:
                return (depth, my_parent)
        return (depth, my_parent)
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # find x, then return depth of x
        x_depth, x_parent = Solution.get_depth(root, root, x, 0)
        if x_depth < 1:
            return False
        
        y_depth, y_parent = Solution.get_depth(root, root, y, 0)
        if y_depth < 1:
            return False
        
        return x_depth == y_depth and x_parent != y_parent
        # find y, then return depth of y
    
        