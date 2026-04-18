# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isSameTree(p,q):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if p.val == q.val:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
            return False
        
        if root.val==subRoot.val:
            if isSameTree(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or  self.isSubtree(root.right,subRoot)
        