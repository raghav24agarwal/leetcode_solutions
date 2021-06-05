# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        first = head
        
        while first.next is not None:
            if first.val == first.next.val:
                first.next = first.next.next
            else:
                first = first.next
                
        return head