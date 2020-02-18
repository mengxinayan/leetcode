# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        elif (head.next == None) and head.val == val:
            return None
        elif (head.next == None) and head.val != val:
            return head
        else:
            while (head != None) and (head.val == val):
                head = head.next
            if head == None:
                return None
            elif head.next == None:
                return head
            else:
                prev = head
                curr = head.next
                while curr != None:
                    if curr.val == val:
                        prev.next = curr.next
                        curr = prev.next
                    else:
                        curr = curr.next
                        prev = prev.next
            return head

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
