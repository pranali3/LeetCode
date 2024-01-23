from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder
        # TC: O(n)
        # SC: O(n)

        arr = []

        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)

        inorder(root)
        return arr[k - 1]
