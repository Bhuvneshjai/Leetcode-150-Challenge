'''
Reverse Linked List II: Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        curr = prev.next
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

# Helper to convert Python list to Linked List
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper to convert Linked List to Python list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
head = list_to_linkedlist([1, 2, 3, 4, 5])
left, right = 2, 4
sol = Solution()
new_head = sol.reverseBetween(head, left, right)
print(linkedlist_to_list(new_head))  # Output: [1, 4, 3, 2, 5]