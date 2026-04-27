# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p1,p2):
            if p1 and not p2 or p2 and not p1:
                return False
            if not p1 and not p2:
                return True
            if p1.val == p2.val:
                return isSameTree(p1.left,p2.left) and isSameTree(p1.right,p2.right)
            return False
        if not root:
            return False
        
        if not subRoot:
            return False

        if subRoot.val == root.val and isSameTree(root,subRoot):
            if isSameTree(root,subRoot):
                return True
            
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)