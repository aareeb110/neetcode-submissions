# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # implement iteratively using stack
        if not root:
            return True
        stack = []
        prev_val = float('-inf')
        curr = root
        while curr or stack:
            # traverse left as far as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()

            if node.val <= prev_val: return False

            # update prev value
            prev_val = node.val
            curr = node.right
        return True