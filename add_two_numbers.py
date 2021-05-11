# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        result = ListNode()
        res = result
        carry = 0
        
        while (l1 is not None and l2 is not None):
            summ = l1.val+l2.val+carry
            
            if summ>9:
                summ = summ%10
                carry = 1
            else:
                carry = 0
                
            temp = ListNode(summ)
                
            if result is None:
                result = temp
                res = temp
            else:
                result.next = temp
                result = temp
            
            l1 = l1.next
            l2 = l2.next
            
        if l1 is None:
            while l2 is not None:
                summ = l2.val+carry
                
                if summ>9:
                    summ = summ%10
                    carry = 1
                else:
                    carry = 0
                
                temp = ListNode(summ)
                
                result.next = temp
                result = temp
                
                l2 = l2.next
                
        else:
            while l1 is not None:
                summ = l1.val+carry
                
                if summ>9:
                    summ = summ%10
                    carry = 1
                else:
                    carry = 0
                
                temp = ListNode(summ)
                
                result.next = temp
                result = temp
                
                l1 = l1.next
                
        if carry!=0:
            result.next = ListNode(carry)
                
        return res.next
                
        
        