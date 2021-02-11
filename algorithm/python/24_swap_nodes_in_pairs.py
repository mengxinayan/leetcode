# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Solution 1: Change values

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
        curr = head
        i = 0
        while curr != None:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head


# Solution 2: Change nodes

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        temp = dummy
        while (temp.next != None) and (temp.next.next != None):
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummy.next


# Solution 3: Recursion

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (head == None) or (head.next == None):
            return head
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head

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
