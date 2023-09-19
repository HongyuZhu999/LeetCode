#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: return list2
        if not list2: return list1

        lil, big = (list1, list2) if list1.val < list2.val else (list2, list1)
        lil.next = self.mergeTwoLists(lil.next, big)
        
        return lil


        '''
        res = NewList = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                NewList.next = list1
                list1 = list1.next
            else:
                NewList.next = list2
                list2 = list2.next
            NewList = NewList.next
        if list1:
            NewList.next = list1
        elif list2:
            NewList.next = list2
        return res.next  
        '''

        

# @lc code=end

