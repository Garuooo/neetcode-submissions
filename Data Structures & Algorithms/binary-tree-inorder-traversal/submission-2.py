# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## inorder == left root right
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            current = stack.pop()
            if not current:
                continue 

            if not current.left and not current.right:
                result.append(current.val)
                continue
            
            left = current.left
            right = current.right
            current.left = None
            current.right = None
            if right:
                stack.append(right)

            stack.append(current)
            if left:
                stack.append(left)

        return result


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        current = root
        stack = []
        res = []


        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res
