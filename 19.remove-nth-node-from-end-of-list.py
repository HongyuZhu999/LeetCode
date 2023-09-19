#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # find the Nth  
        tmp1, tmp2 = dummy, head
        count = 1
        while count <= n and tmp2:
            tmp2 = tmp2.next
            count += 1
        while tmp2:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        # delete
        tmp1.next = tmp1.next.next
        return dummy.next

            

# @lc code=end

