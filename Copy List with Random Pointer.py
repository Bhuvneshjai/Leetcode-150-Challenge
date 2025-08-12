'''
Copy List with Random Pointer: A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node
has its value set to the value of its corresponding original node. Both the next and random pointer of the new
nodes should point to new nodes in the copied list such that the pointers in the original list and copied list
represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of
[val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does
not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
'''

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        old_to_new = {}

        # 1️⃣ First pass: clone nodes (values only)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 2️⃣ Second pass: assign next and random pointers
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]


def build_linked_list_with_random(nodes):
    """
    nodes: List of [val, random_index]
    random_index: int (index in list) or None
    """
    if not nodes:
        return None

    node_list = [Node(val) for val, _ in nodes]

    # Link next pointers
    for i in range(len(node_list) - 1):
        node_list[i].next = node_list[i + 1]

    # Link random pointers
    for i, (_, rand_index) in enumerate(nodes):
        if rand_index is not None:
            node_list[i].random = node_list[rand_index]

    return node_list[0]  # head


def linked_list_to_list(head):
    """
    Converts linked list with random pointers into [val, random_index]
    """
    if not head:
        return []

    node_to_index = {}
    nodes = []
    curr = head
    idx = 0
    while curr:
        node_to_index[curr] = idx
        nodes.append(curr)
        curr = curr.next
        idx += 1

    result = []
    for node in nodes:
        rand_idx = node_to_index[node.random] if node.random else None
        result.append([node.val, rand_idx])
    return result


# 🧪 Example test
nodes_data = [
    [7, None],
    [13, 0],
    [11, 4],
    [10, 2],
    [1, 0]
]

head = build_linked_list_with_random(nodes_data)
sol = Solution()
copied_head = sol.copyRandomList(head)

print("Original List:", linked_list_to_list(head))
print("Copied List:  ", linked_list_to_list(copied_head))
