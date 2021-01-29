# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def recursion(l1: ListNode, l2: ListNode, t:int, curr: ListNode):
            if (l1 == None) and (l2 == None):
                if t != 0:
                    cur.next = ListNode(t)
                    t = 0
                    recursion(l1, l2, t, curr.next)
                else:
                    pass
            elif (l1 == None) and (l2 != None):
                tmp = l2.val + t
                curr.next = ListNode(tmp%10)
                t = tmp // 10
                recursion(l1, l2.next, t, curr.next)
            elif (l1 != None) and (l2 == None):
                tmp = l1.val + t
                curr.next = ListNode(tmp%10)
                t = tmp // 10
                recursion(l1.next, l2, t, curr.next)
            else:
                tmp = l1.val + l2.val + t
                curr.next = ListNode(tmp % 10)
                t = tmp // 10
                recursion(l1.next, l2.next, t, curr.next)

        t = 0
        curr = ListNode()
        res_head = curr
        recursion(l1, l2, t, curr)
        res_head = res_head.next
        return res_head

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
