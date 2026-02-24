# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev = dummy
        temp = prev.next
        nums = set()

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next

                prev.next = head.next
                head.next = None
            else:
                prev = prev.next
            head = prev.next

        
        return dummy.next