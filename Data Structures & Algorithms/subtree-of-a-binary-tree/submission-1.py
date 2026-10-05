# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def checkSame(root1, root2):
            if not root1 and not root2:
                return True

            if (not root1 and root2) or (root1 and not root2):
                return False
            if root1.val != root2.val:
                return False

            left = checkSame(root1.left, root2.left)
            right = checkSame(root1.right, root2.right)

            return (left and right)

  
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False

        if checkSame(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)      
       