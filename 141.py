from typing import Optional


class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    # TC: O(n)
    # SC: O(1)
    # curr = head
    # prev_dict = {}
    # prev = None

    # while curr:
    #     if curr in prev_dict:
    #         return True
    #     prev_dict[curr] = prev
    #     prev = curr
    #     curr = curr.next
    # return False

    while head:
        if head.val == 10 ** 6:
            return True
        head.val = 10 ** 6
        head = head.next
    return False
