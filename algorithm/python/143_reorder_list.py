# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def find_mid_node(head: ListNode) -> ListNode:
            slow = fast = head
            while (fast != None) and (fast.next != None):
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_list(head: ListNode) -> ListNode:
            if (head == None) or (head.next == None):
                return head
            curr_pre = None
            curr = head
            curr_next = curr
            while curr != None:
                curr_next = curr.next
                curr.next = curr_pre
                curr_pre = curr
                curr = curr_next
            return curr_pre

        if (head == None) or (head.next == None):
            return 
        mid_node = find_mid_node(head)
        second_half = mid_node.next
        second_half = reverse_list(second_half)
        mid_node.next = None
        p1 = head
        p2 = second_half
        while (p1 != None) and (p2 != None):
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p1 = tmp1
            p2.next = p1
            p2 = tmp2

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020  mengxinayan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
