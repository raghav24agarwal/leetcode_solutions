# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        len1 = 0
        first = headA
        
        while first is not None:
            len1+=1
            first = first.next
            
        len2 = 0
        second = headB
        
        while second is not None:
            len2+=1
            second = second.next
            
        if len1>len2:
            diff = len1-len2
            third = headA
            fourth = headB
            
        else:
            diff = len2-len1
            third = headB
            fourth = headA

        while diff!=0:
            third = third.next
            diff-=1
            
        while third is not None and fourth is not None:
            if third == fourth:
                return third
            
            third = third.next
            fourth = fourth.next
            
        return None