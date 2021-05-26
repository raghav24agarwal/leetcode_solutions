# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head is None or k==0:
            return head
        
        start = head
        length = 1
        
        while start.next is not None:
            start = start.next
            length+=1
            
        tail = start
        
        rotation_point = length - (k%length)
        
        counter = 1
        start = head
        
        while counter<rotation_point:
            start = start.next
            counter+=1
            
        if start.next is None:
            return head
        else:
            tail.next = head
            head = start.next
            start.next = None

        return head