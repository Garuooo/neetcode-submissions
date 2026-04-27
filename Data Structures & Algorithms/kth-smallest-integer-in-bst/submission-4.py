# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def morris_inorder(root):
            nonlocal k
            current = root

            while current:
                if not current.left:
                    k -= 1
                    if k == 0:
                        return current.val
                    current = current.right
                else:
                    prev = current.left
                    while prev.right and prev.right != current:
                        prev = prev.right

                    if not prev.right:
                        prev.right = current
                        current = current.left
                    else:
                        prev.right = None
                        k -= 1
                        if k == 0:
                            return current.val
                        current = current.right
            return res
        return morris_inorder(root)