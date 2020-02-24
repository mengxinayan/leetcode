# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def recursive(root: TreeNode, path: str, path_array:List[str]):
            if root == None:
                return ''
            elif (root != None) and (root.left == None) and (root.right == None):
                path += str(root.val)
                path_array.append(path)
            else:
                path += str(root.val) + '->'
                recursive(root.left, path, path_array)
                recursive(root.right, path, path_array)

        if root == None:
            return []
        else:
            path = ''
            path_array = []
            recursive(root, path, path_array)
            return path_array

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
