# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next
        # Checking of empty LL
        # if head is None or head.next is None:
        #     return None
        # Storing head to temp variable
        # temp = head
        # assigning slow pointer at temp(head)
        # slow = temp
        # Checking for the end node i.e. null 
        # while temp:
        #     # move slow pointer by one step
        #     if temp.val == node:
        #         temp.next = temp.next.next 
        #     temp = temp.next
            
        # return head.next
        
        