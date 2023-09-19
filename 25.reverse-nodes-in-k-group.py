#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0, head)

        while True:
            kth = self.getk(groupPrev, k)
            if not kth:
                break
            groupPrev.next = kth
            groupNext = kth.next

            #reverse
            curr, prev = head, groupNext
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            groupPrev = head
            head = groupNext
        
        return dummy.next

        
    def getk(self, head, k):
        while k > 0 and head:
            head = head.next
            k -= 1
        return head

# @lc code=end

