# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Storing head to temp variable
        temp = head
        # assigning slow pointer to temp(head)
        slow = temp
        # assigning fast pointer to temp(head)
        fast = temp
        # Checking for the end node i.e. null
        while fast and fast.next:
            # move slow pointer by one step
            slow = slow.next
            # move fast pointer by two step
            fast = fast.next.next
            # Checking slow and fast pointer collision
            if slow == fast:
                slow = head
                while slow != fast:
                # returning true in case of collision or loop
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


# Time Complexity --    O(N)  as it traverse one time
# Space Complexity --   O(1)  as it not use any extra space
