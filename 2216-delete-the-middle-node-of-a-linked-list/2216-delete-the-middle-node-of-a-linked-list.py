# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        # Storing head to temp variable
        temp = head
        # assigning slow pointer at temp(head)
        slow = temp
        # assigning fast pointer at temp(head)
        fast = temp
        fast = temp.next.next if temp.next else None
        # Checking for the end node i.e. null 
        while(fast and fast.next):
            # move slow pointer by one step
            slow = slow.next
            # move fast pointer by two step
            fast = fast.next.next
            # if slow == fast:
        slow.next = slow.next.next 
        return head
        # if head is None or head.next is None:
        #     return None

        # # Initialize slow and fast pointers
        # slow = head
        # fast = head.next.next if head.next else None

        # # Move 'fast' pointer twice as fast as 'slow'
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # # Delete the middle node by skipping it
        # slow.next = slow.next.next
        # return head
