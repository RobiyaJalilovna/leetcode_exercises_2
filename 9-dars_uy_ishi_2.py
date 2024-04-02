# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: []) -> int:
        if not root:
            return 0

        d=0
        q=[root]
        while q:
            d+=1
            ns=[]
            while q:
                ns.append(q.pop())
            while ns:
                n = ns.pop()
                if not n.left and not n.right:
                    return d
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return d