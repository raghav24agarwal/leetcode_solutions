# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        new_list = None
        new_head = None
        
        #appending a node to left of original node
        before = ListNode(0)
        before.next = head
        
        first = before
        while(first.next is not None):
            if first.next.val<x:
                if new_list is None:
                    new_list = ListNode(first.next.val)
                    new_head = new_list
                else:
                    new_list.next = ListNode(first.next.val)
                    new_list = new_list.next
                    
                #deleting the node with smaller value from original list
                first.next = first.next.next
                
            else:
                first = first.next
                
        #if no value is smaller than x,
        #new_head will be None and
        #we can return the original list
        if new_head is None:
            return head
        
        #appending the original list with no smaller elements
        #to the right of the newly created list with smaller elements
        new_list.next = before.next
        
        return new_head