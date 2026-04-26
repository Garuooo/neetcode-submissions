# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            smallest = p
            biggest = q
        else:
            smallest = q
            biggest = p


        if smallest.val <= root.val <= biggest.val:
            return root
        elif root.left and root.val >= biggest.val:
            root=root.left
            return self.lowestCommonAncestor(root,p,q)
        elif root.right:
            root = root.right
            return self.lowestCommonAncestor(root,p,q)
        
        return root
