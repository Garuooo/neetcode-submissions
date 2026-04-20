# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
            
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root,1)]
        while stack:
            current,level = stack.pop()
            print(current,level)
            if current.left:
                stack.append((current.left,level+1))
            if current.right:
                stack.append((current.right,level+1))

            if not current.left and not current.right:
                res = max(res,level)
        return res