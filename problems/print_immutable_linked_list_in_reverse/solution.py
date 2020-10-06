# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

from collections import deque


# This would be linear time complexity O(n) for n = the length of the immutable nodes
# it is [maybe] < linear space complexity since we are just storing 
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        d = deque()
        current_node = head
        while current_node != None:
            d.append(current_node.printValue)
            current_node = current_node.getNext()
        d.reverse()
        for func in d:
            func()