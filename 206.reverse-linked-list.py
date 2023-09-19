#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive: T O(n), M O(n)
        # Test: List = [1, 2, 3]

        if not head:
            return None
        
        newHead = head
        # newHead = [1, 2, 3]
        if head.next:
            newHead = self.reverseList(head.next)
            # *2 reverseList([2, 3]) newHead = [2, 3]
            # *3 reverseList([3]) newHead = [3] 
            #       head.next = None return [3]
            # *2 newhead = [3]  head.next.next = [2] head = [2, 3, 2]
            head.next.next = head 
            # now we konw in the list 2->3 3->2, we need 3->2
            # so use head.next = none to break 2->3, and we only have 3->2
        head.next = None
        # hard to understand

        return newHead

'''
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
'''

# @lc code=end

