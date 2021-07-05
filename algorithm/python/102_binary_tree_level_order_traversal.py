# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def level_traversal(parents: List[TreeNode]):
            if len(parents) == 0:
                pass
            else:
                tmp_val = []
                tmp_node = []
                for tree_node in parents:
                    if tree_node.left != None:
                        tmp_node.append(tree_node.left)
                        tmp_val.append(tree_node.left.val)
                    if tree_node.right != None:
                        tmp_node.append(tree_node.right)
                        tmp_val.append(tree_node.right.val)
                if len(tmp_val) != 0:
                    ans.append(tmp_val)
                level_traversal(tmp_node)

        if root == None:
            return []
        ans = [[root.val]]
        level_traversal([root])
        return ans

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
