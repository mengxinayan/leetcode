# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1: calculate length(without dummy node)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        length = 0
        while curr != None:
            length += 1
            curr = curr.next
        target = length - n
        if target == 0:
            return head.next
        curr = head
        i = 1
        while i < target:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head


# Solution 2: calculate length(with dummy node)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        curr = dummy
        length = 0
        while curr != None:
            length += 1
            curr = curr.next
        target = length - n
        curr = dummy
        i = 1
        while i < target:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return dummy.next


# Solution 3: Stack(with dummy node)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        curr = dummy
        stack = []
        while curr != None:
            stack.append(curr)
            curr = curr.next
        for i in range(n):
            stack.pop()
        node = stack[-1]
        node.next = node.next.next
        return dummy.next


# Solution 4: Two Pointers(with dummy node)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

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
