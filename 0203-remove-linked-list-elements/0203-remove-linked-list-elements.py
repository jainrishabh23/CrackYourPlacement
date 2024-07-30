# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # temp = head

        # while temp and temp.next :
        #     if temp.val == val:
        #         temp.next = temp.next.next
        # return head

        # dummy = ListNode(0, head)
        # temp = dummy

        # making dummy LL
        dummy = ListNode(0,head)
        temp = dummy
        curr = head
        while curr:
            nxt = curr.next
            if curr.val == val:
                temp.next = nxt
            else:
                temp = curr

            curr = nxt

        return dummy.next
