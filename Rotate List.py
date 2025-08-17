'''
Rotate List: Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k = k%length
        if k == 0:
            return head
        tail.next = head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

def to_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
head = to_linked_list([1,2,3,4,5])
sol = Solution()
new_head = sol.rotateRight(head, 2)
print(to_list(new_head))  # Output: [4,5,1,2,3]

head = to_linked_list([0,1,2])
new_head = sol.rotateRight(head, 4)
print(to_list(new_head))  # Output: [2,0,1]
