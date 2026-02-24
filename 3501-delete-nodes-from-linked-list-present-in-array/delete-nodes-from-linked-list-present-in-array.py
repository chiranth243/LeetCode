# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not nums:
            return head

        if not head:
            return None

        num_set = set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        temp = prev.next

        while temp:
            if temp.val in num_set:
                prev.next = temp.next
                temp.next = None
            else:
                prev = prev.next
            temp = prev.next

        return dummy.next
        