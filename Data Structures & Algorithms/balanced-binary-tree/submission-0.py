# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def calcHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.calcHeight(root.left)
        right = self.calcHeight(root.right)

        if left == -1 or right ==-1:
            return -1

        height = abs(left - right) 

        if height > 1:
            return -1

        return 1 + max(left, right)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        left = self.calcHeight(root.left)
        right = self.calcHeight(root.right)

        if left == -1 or right == -1:
            return False

        height = abs(left - right)
        if height > 1:
            return False

        return True


        