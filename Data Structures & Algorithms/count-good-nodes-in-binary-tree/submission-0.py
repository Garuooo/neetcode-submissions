# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes=[]
        def dfs(root,maximum=float("-inf")):
            if not root:
                return 
            maximum=max(root.val,maximum)
            if maximum == root.val:
                good_nodes.append(root)
            dfs(root.left,maximum)
            dfs(root.right,maximum)
        dfs(root)
        return len(good_nodes)
