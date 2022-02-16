# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorder_map = { inorder[i]: i for i in range(0, n) }
        root = TreeNode(preorder[0])

        def insert(node, val):
            if inorder_map[node.val] < inorder_map[val]:
                if node.right:
                    insert(node.right, val)
                else:
                    node.right = TreeNode(val)
            elif inorder_map[node.val] > inorder_map[val]:
                if node.left:
                    insert(node.left, val)
                else:
                    node.left = TreeNode(val)
        for e in preorder[1:]:
            insert(root, e)

        return root



