'''
Partition List: Given the head of a linked list and a value x, partition it such that all nodes less than x come
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

from typing import Optional
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head
        curr = head

        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next

        after.next = None                # end the "after" list
        before.next = after_head.next    # join the two lists (skip dummy node)

        return before_head.next


# 🔹 Helpers
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


# 🔹 Example usage
head = to_linked_list([1,4,3,2,5,2])
sol = Solution()
new_head = sol.partition(head, 3)
print(to_list(new_head))  # ✅ [1,2,2,4,3,5]

head = to_linked_list([2,1])
new_head = sol.partition(head, 2)
print(to_list(new_head))  # ✅ [1,2]
