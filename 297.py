class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # TC: O(n)
        # SC: O(1)

        res = []

        def preorder(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # TC: O(n)
        # SC: O(1)
        vals = data.split(",")

        def preorder():
            if vals:
                val = vals.pop(0)
                if val == "N":
                    return
                node = TreeNode(int(val))
                node.left = preorder()
                node.right = preorder()
            return node

        return preorder()
