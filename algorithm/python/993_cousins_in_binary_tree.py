# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def dfs(node: TreeNode, parent: int):
            if node != None:
                if parent != None:
                    self.depth_dict[node.val] = 1 + self.depth_dict[parent.val]
                else:
                    self.depth_dict[node.val] = 0
                self.parent_dict[node.val] = parent
                dfs(node.left, node)
                dfs(node.right, node)

        self.depth_dict = {}
        self.parent_dict = {}
        dfs(root, None)
        return (self.depth_dict[x] == self.depth_dict[y]) and (self.parent_dict[x] != self.parent_dict[y])

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
