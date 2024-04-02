# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: []) -> bool:
        def traverse(root):
            if not root:
                return 0

            leftH = traverse(root.left)
            # left subtree is not balanced.
            if leftH == -1:
                return -1
            rightH = traverse(root.right)
            # right subtree is not balanced
            if rightH == -1:
                return -1

            if abs(leftH - rightH) > 1:
                return -1
            return max(leftH, rightH) + 1

        return traverse(root) != -1