"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        curr = dummy
        index_node_dict = {}
        node_index_dict = {}
        tmp = head
        index = 0
        while tmp != None:
            temp_node = Node(tmp.val)
            index_node_dict[index] = temp_node
            node_index_dict[tmp] = index
            curr.next = temp_node
            curr = curr.next
            tmp = tmp.next
            index += 1
        curr = dummy.next
        tmp = head
        index = 0
        while tmp != None:
            if tmp.random != None:
                curr.random = index_node_dict[node_index_dict[tmp.random]]
            tmp = tmp.next
            curr = curr.next
            index += 1
        return dummy.next

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
