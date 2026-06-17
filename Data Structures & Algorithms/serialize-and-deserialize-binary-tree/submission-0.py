# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def preorder(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(vals)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.index = 0

        def build_tree():
            if self.index >= len(vals) or vals[self.index] == "null":
                self.index += 1
                return None
            
            node = TreeNode(int(vals[self.index]))
            self.index += 1
            node.left = build_tree()
            node.right = build_tree()
            return node
        return build_tree()
