# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: [], targetSum: int) -> bool:

        def helper(node, ssf, targetSum):
            if (node == None):
                return False

            ssf += node.val
            if (node.left == None and node.right == None):
                if (ssf == targetSum):
                    return True
                return False

            return helper(node.left, ssf, targetSum) or helper(node.right, ssf, targetSum)

        return helper(root, 0, targetSum)