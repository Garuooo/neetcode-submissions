class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum=float("-inf")
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left) 
            right = dfs(root.right)
            leftMax = max(left,0)
            rightMax = max(right,0)
            self.max_sum = max(self.max_sum,leftMax+rightMax+root.val)
            return max(leftMax+root.val,rightMax+root.val)
        dfs(root)
        return self.max_sum