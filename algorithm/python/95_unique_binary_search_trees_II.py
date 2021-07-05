# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generate_BST(begin: int, end: int) -> List[TreeNode]:
            if begin > end:
                return [None,]
            all_trees = []
            for i in range(begin, end+1):
                left_tree = generate_BST(begin, i-1)
                right_tree = generate_BST(i+1, end)
                for l in left_tree:
                    for r in right_tree:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right =r
                        all_trees.append(curr)
            return all_trees
        
        if n != 0:
            return generate_BST(1, n)
        else:
            return []

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
