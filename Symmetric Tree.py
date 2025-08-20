'''
Symmetric Tree: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around
its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
'''

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Public API: pick either recursive or iterative under the hood
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # You can switch to self.isSymmetric_iter(root) if you prefer iterative
        return self.isSymmetric_rec(root)

    # ---- Recursive ----
    def isSymmetric_rec(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (a.val == b.val
                    and isMirror(a.left, b.right)
                    and isMirror(a.right, b.left))

        return isMirror(root.left, root.right)

# Build a symmetric tree: [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

sol = Solution()
print(sol.isSymmetric(root))        # True

# Asymmetric tree: [1,2,2,None,3,None,3]
root2 = TreeNode(1)
root2.left = TreeNode(2, None, TreeNode(3))
root2.right = TreeNode(2, None, TreeNode(3))

print(sol.isSymmetric(root2))       # False

