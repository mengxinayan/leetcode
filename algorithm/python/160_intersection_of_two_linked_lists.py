# Solution 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None) or (headB == None):
            return None
        node_id_A = set([])
        p = headA
        while p != None:
            node_id_A.add(id(p))
            p = p.next
        q = headB
        while q != None:
            if id(q) in node_id_A:
                return ListNode(q.val)
            q = q.next
        return None


# Solution 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None) or (headB == None):
            return None
        p = headA
        q = headB
        while p.next != None:
            p = p.next
        while q.next != None:
            q = q.next
        if p.val != q.val:
            return None
        else:
            p = headA
            q = headB
            while p != q:
                if p.next == None and q.next != None:
                    p = headB
                    q = q.next
                elif q.next == None and p.next != None:
                    q = headA
                    p = p.next
                else:
                    p = p.next
                    q = q.next
            if p == None:
                return None
            else:
                return ListNode(p.val)

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
    MERCHANTABILITY or FITNESS FOR A pRTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''