# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        ## to get the sorted list of elements:
        ## we should do a inorder search

        def morris_inorder(root):
            res = []

            current = root


            while current:
                if not current.left:
                    res.append(current.val)
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
                        res.append(current.val)
                        current = current.right
            return res
        return morris_inorder(root)[k-1]