#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            res = []
            # merge every two list each time
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                res.append(self.mergeList(list1, list2))
            lists = res
        return lists[0]    

    # merge two Lists 
    def mergeList(self, list1, list2):

        if not list1: return list2
        if not list2: return list1
        
        res, biggerval = (list1, list2) if list1.val < list2.val else (list2, list1)
        res.next = self.mergeList(res.next, biggerval)

        return res
'''
    def mergeList(self, l1, l2):
        dummy = node = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 or l2
        return dummy.next
'''

# @lc code=end

