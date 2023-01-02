from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if (head is not None) and (head.next is None):
            return head
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
        head = None
        tail = None
        for idx in range(len(list_vals)-1, -1, -1):
            node = ListNode(list_vals[idx])
            if head is None:
                head = node
                tail = head
            tail.next = node
            tail = tail.next
        return head