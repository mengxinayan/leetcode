"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def get_next_node(root: 'Node') -> 'Node':
            if root == None:
                return None
            if root.left != None:
                return root.left
            if root.right != None:
                return root.right
            if root.next != None:
                return get_next_node(root.next)
            return None

        def dfs(root: 'Node') -> 'Node':
            if root == None:
                return root
            if (root.left != None) and (root.right != None):
                root.left.next = root.right
            if (root.left != None) and (root.right == None):
                root.left.next = get_next_node(root.next)
            if (root.right != None):
                root.right.next = get_next_node(root.next)
            dfs(root.right)
            dfs(root.left)
            return root
        
        root = dfs(root)
        return root

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2022  mengxinayan

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
