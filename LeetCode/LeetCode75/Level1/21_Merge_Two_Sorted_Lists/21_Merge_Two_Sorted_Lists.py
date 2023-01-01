from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 is None) and (list2 is None):
            return None

        result_list = []

        while list1:
            result_list.append(list1.val)
            list1 = list1.next

        while list2:
            result_list.append(list2.val)
            list2 = list2.next

        result_list = sorted(result_list)
        if result_list:
            result_head = None
            result_curr_pointer = None
            for elem in result_list:
                if result_head is None:
                    result_head = ListNode(elem)
                    result_curr_pointer = result_head
                    continue
                node = ListNode(elem)
                result_curr_pointer.next = node
                result_curr_pointer = result_curr_pointer.next
            return result_head


if __name__ == "__main__":
    sol = Solution()
    testcases = []
    l1_elem2 = ListNode(4, None)
    l1_elem1 = ListNode(2, l1_elem2)
    l1_elem1 = ListNode(1, l1_elem2)
    l2_elem2 = ListNode(4, None)
    l2_elem1 = ListNode(3, l2_elem2)
    l2_elem1 = ListNode(1, l2_elem2)
    testcases.append((l1_elem1, l2_elem1))
    testcases.append((None, None))
    testcases.append((None, ListNode(0, None)))

    for t_case_num, t_case_ip in enumerate(testcases):
        list1 = t_case_ip[0]
        list2 = t_case_ip[1]
        r = sol.mergeTwoLists(list1, list2)
        print(f"Test Case Number: {t_case_num+1}")
        print(f"Inputs:\ns={list1}\tt={list2}\n")
        print(f"Output: {r}\n")
        print("#" * 30)
        print("\n")
