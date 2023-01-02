from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def detectCycleAccepted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or ((head is not None) and (head.next is None)):
            return None
        result = [head]
        curr = head.next
        while curr:
            if curr.next in result:
                return result[result.index(curr.next)]
            if curr in result:
                return result[result.index(curr)]
            result.append(curr)
            curr = curr.next
        return None


    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or ((head is not None) and (head.next is None)):
            return None
        result = {head}
        curr = head.next
        while curr:
            if curr.next in result:
                return curr.next
            if curr in result:
                return curr
            result.add(curr)
            curr = curr.next
        return None