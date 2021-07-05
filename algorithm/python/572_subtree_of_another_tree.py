# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def is_same_tree(s: TreeNode, t: TreeNode) -> bool:
            if s == None and t == None:
                return True
            elif s != None and t != None:
                return (s.val == t.val) and (is_same_tree(s.left, t.left)) and (is_same_tree(s.right, t.right))
            else:
                return False

        if s == None and t == None:
            return True
        elif s != None and t != None:
            return is_same_tree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False

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
