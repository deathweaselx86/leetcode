# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_node0 = l1
        current_node1 = l2
        carry = 0
        
        
        result_digits = deque()
        while current_node0 or current_node1:
            new_digit = carry
            if current_node0:
                new_digit = new_digit + current_node0.val
                current_node0 = current_node0.next
            if current_node1:
                new_digit = new_digit + current_node1.val
                current_node1 = current_node1.next
                
            if new_digit > 9:
                carry = 1
                new_digit = new_digit - 10
            else:
                carry = 0
            result_digits.append(new_digit)
        if carry > 0:
            result_digits.append(carry)
            
        resultRoot = ListNode(val=result_digits.popleft())
        currentNode = resultRoot
        while len(result_digits) > 0:
            currentNode.next = ListNode(val=result_digits.popleft())
            currentNode = currentNode.next
        return resultRoot