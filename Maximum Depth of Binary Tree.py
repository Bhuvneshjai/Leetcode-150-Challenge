'''
Maximum Depth of Binary Tree: Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.right = right
        self.left = left

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def build_tree(nodes: list[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    index = 1

    while queue and index < len(nodes):
        current = queue.popleft()
        if index < len(nodes) and nodes[index] is not None:
            current.left = TreeNode(nodes[index])
            queue.append(current.left)
        index += 1

        if index < len(nodes) and nodes[index] is not None:
            current.right = TreeNode(nodes[index])
            queue.append(current.right)
        index += 1

    return root

# Input list representing binary tree level-order
tree_list = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_list)

sol = Solution()
print(sol.maxDepth(root))  # Output: 3
