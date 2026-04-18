# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        print(root.val,p.val,q.val)
        if p.val < q.val:
            left = p
            right=q
        else:
            left=q
            right=p
        if not root:
            return
        if left.val <= root.val <= right.val:
            return root
        elif root.val >= left.val and root.val >= right.val :
            return self.lowestCommonAncestor(root.left, left, right)
        else:
            return self.lowestCommonAncestor( root.right, left, right)
