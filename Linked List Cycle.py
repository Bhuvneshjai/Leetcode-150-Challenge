'''
Linked List Cycle: Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# --- Example test usage ---
def create_linked_list_with_cycle(values, pos):
    """
    values: List of node values
    pos: Index to connect tail to (0-indexed). -1 means no cycle.
    Returns head of the linked list.
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        node = ListNode(val)
        current.next = node
        current = node
        nodes.append(node)

    if pos != -1:
        current.next = nodes[pos]  # Create the cycle

    return head

# Example 1: Cycle exists
head1 = create_linked_list_with_cycle([3,2,0,-4], 1)
print(Solution().hasCycle(head1))  # Output: True

# Example 2: Cycle exists
head2 = create_linked_list_with_cycle([1,2], 0)
print(Solution().hasCycle(head2))  # Output: True

# Example 3: No cycle
head3 = create_linked_list_with_cycle([1], -1)
print(Solution().hasCycle(head3))  # Output: False