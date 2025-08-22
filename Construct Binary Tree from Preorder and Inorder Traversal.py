'''
Construct Binary Tree from Preorder and Inorder Traversal: Given two integer arrays preorder and inorder where
preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map value -> index in inorder for O(1) lookup
        inorder_index = {val: idx for idx, val in enumerate(inorder)}

        # Iterator over preorder list
        self.pre_idx = 0

        def array_to_tree(left, right):
            if left > right:
                return None

            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Build left and right subtrees
            root.left = array_to_tree(left, inorder_index[root_val] - 1)
            root.right = array_to_tree(inorder_index[root_val] + 1, right)
            return root

        return array_to_tree(0, len(inorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

sol = Solution()
root = sol.buildTree(preorder, inorder)

# Simple inorder traversal print to verify
def inorder_traversal(node):
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right) if node else []

print(inorder_traversal(root))