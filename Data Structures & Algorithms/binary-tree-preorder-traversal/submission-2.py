# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        while stack:
            current = stack.pop()

            if not current:
                continue
            
            if not current.left and not current.right:
                res.append(current.val)
                continue 

            left = current.left
            right = current.right
            current.left = None
            current.right = None
            stack.append(right)
            stack.append(left)
            stack.append(current)
        
        return res


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        current = root
        while stack or current:
            while current:
                res.append(current.val)
                stack.append(current)
                current=current.left

            current = stack.pop()
            current = current.right
        
        return res