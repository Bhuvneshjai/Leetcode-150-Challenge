'''
Reverse Nodes in k-Group: Given the head of a linked list, reverse the nodes of the list k at a time, and return
the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not
a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev, curr = end, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev= curr
                curr = nxt
            return prev
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while count >= k:
            tail = curr
            for _ in range(k):
                curr = curr.next
            prev.next = reverse(tail, curr)
            prev = tail
            count -= k
        return dummy.next

# Helper to convert list to linked list
def to_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper to convert linked list to list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
head = to_linked_list([1,2,3,4,5])
sol = Solution()
new_head = sol.reverseKGroup(head, 2)
print(to_list(new_head))  # Output: [2,1,4,3,5]