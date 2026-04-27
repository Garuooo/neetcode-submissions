# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = []
        def dfs(root,maximum):
            if not root:
                return

            if maximum <= root.val:
                res.append(root.val)

            dfs(root.left,max(maximum,root.val))
            dfs(root.right,max(maximum,root.val))
        dfs(root,float("-inf"))
        return len(res)