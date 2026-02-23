# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head:
            return None

        sum = 0
        temp = head

        while temp:
            sum = (sum*2) + temp.val
            temp = temp.next

        return sum
        