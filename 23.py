from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # TC: O(n*logk)
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # TC: O(n+m)
            # SC: O(n+m)

            if not list1 and not list2:
                return None
            if not list1 and list2:
                return list2
            if not list2 and list1:
                return list1

            list3 = dummy = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    list3.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    list3.next = ListNode(list2.val)
                    list2 = list2.next
                list3 = list3.next

            while list1:
                list3.next = ListNode(list1.val)
                list3 = list3.next
                list1 = list1.next
            while list2:
                list3.next = ListNode(list2.val)
                list3 = list3.next
                list2 = list2.next
            return dummy.next

        while len(lists) > 1:  # O(n)
            mergedList = []
            for i in range(0, len(lists), 2):  # O(logk)
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(mergeTwoLists(l1, l2))
            lists = mergedList
        return lists[0]
