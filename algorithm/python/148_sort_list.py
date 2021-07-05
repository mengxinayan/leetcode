# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def sort_list(head: ListNode, tail: ListNode) -> ListNode:
            if head == None:
                return head
            elif head.next == tail:
                head.next = None
                return head
            else:
                fast = slow = head
                mid = None
                while (fast != tail) and (fast.next != tail):
                    slow = slow.next
                    fast = fast.next.next
                mid = slow
                return merge_list(sort_list(head, mid), sort_list(mid, tail))
        
        def merge_list(list1: ListNode, list2: ListNode):
            dummy = ListNode(0)
            temp = dummy
            temp1 = list1
            temp2 = list2
            while (temp1 != None) and (temp2 != None):
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1 != None:
                temp.next = temp1
            if temp2 != None:
                temp.next = temp2
            return dummy.next
        
        return sort_list(head, None)

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2021  mengxinayan

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
