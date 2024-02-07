# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        result_tail = result

        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l2.val + carry
                l2 = l2.next

            carry = 0
            if sum > 9:
                carry = 1
                units_place = sum % 10
            else:
                units_place = sum + carry

            result_tail.next = ListNode(units_place)
            result_tail = result_tail.next

        if carry == 1:
            result_tail.next = ListNode(carry)

        return result.next
