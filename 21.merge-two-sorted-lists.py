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
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not l1:
            return l2

        if not l2:
            return l1

        head_node = None

        if l1.val < l2.val:
            head_node = l1
            l1 = l1.next
        else:
            head_node = l2
            l2 = l2.next

        cur_node = head_node

        while l1 and l2:
            if l1.val < l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next
            cur_node = cur_node.next

        cur_node.next = l1 if l1 else l2

        return head_node


# @lc code=end
