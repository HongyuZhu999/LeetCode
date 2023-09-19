#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reserve second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two half
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        '''
        # Time Limit Exceeded
        def ReverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            res, list_Rs = None, head
            while list_Rs:
                nxt = list_Rs.next
                list_Rs.next = res
                res = list_Rs
                list_Rs = nxt
            return res        
        key = None
        List_Rd = head
        while List_Rd:
            nxt = ReverseList(List_Rd.next)
            List_Rd.next = key
            key = List_Rd
            List_Rd = nxt
        head = ReverseList(key)       
        '''
        """
        Do not return anything, modify head in-place instead.
        """
        
# @lc code=end

