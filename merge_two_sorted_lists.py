# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 is None and l2 is None:
            return None
        
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        first = l1
        second = l2
        
        if first.val<=second.val:
            head = first
            prev = first
            first = first.next
        else:
            head = second
            prev = second
            second = second.next
    
        
        while first is not None and second is not None:
            if first.val<=second.val:
                prev.next = first
                prev = prev.next
                first = first.next
            else:
                prev.next = second
                prev = second
                second = second.next
    
            
        while first is not None:
            prev.next = first
            prev = first
            first = first.next
            
        while second is not None:
            prev.next = second
            prev = second
            second = second.next

            
        return head   
                
            
            
        