# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def calcHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = calcHeight(root.left)
            right = calcHeight(root.right)

            if left == -1 or right ==-1:
                return -1

            height = abs(left - right) 

            if height > 1:
                return -1

            return 1 + max(left, right)

        if not root:
            return isBalanced
            
        left = calcHeight(root.left)
        right = calcHeight(root.right)

        if left == -1 or right == -1 or abs(left-right) > 1:
            isBalanced = False

        return isBalanced


        