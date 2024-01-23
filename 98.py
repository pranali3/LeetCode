from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # TC: O(n)
        # Sc: O(h) # recursive stack space

        def isValid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            # check left and right
            return (isValid(node.left, left, node.val)  # parent is the right boundary for left node
                    and isValid(node.right, node.val, right))  # parent is the left boundary for right node

        return isValid(root, float("-inf"), float("inf"))
