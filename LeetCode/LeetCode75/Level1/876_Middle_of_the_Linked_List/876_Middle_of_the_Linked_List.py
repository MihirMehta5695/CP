from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or ((head is not None) and (head.next is None)):
            return head
        result = [head]
        curr = head.next
        while curr:
            result.append(curr)
            curr = curr.next
        list_len = len(result)
        if list_len//2==1:
            return result[1]
        return result[list_len//2]