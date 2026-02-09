# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        nodes = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)

        def balance(left,right):
            if left>right:
                return None
            mid = (left +right) // 2
            root = nodes[mid]
            root.left = balance(left,mid - 1)
            root.right = balance(mid + 1,right)
            return root 
        return balance(0, len(nodes) - 1)

        