# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def dfs(inorder: List[int], postorder: List[int]):
            if (len(inorder) == 0) or (len(postorder) == 0):
                return None
            if (len(inorder) == 1) and (len(postorder) == 1):
                return TreeNode(inorder[-1])
            index = inorder.index(postorder[-1])
            left_inorder = inorder[:index]
            left_postorder = postorder[:len(left_inorder)]
            right_inorder = inorder[index+1:]
            right_postorder = postorder[len(left_inorder):len(postorder)-1]
            root = TreeNode(postorder[-1])
            root.left = dfs(left_inorder, left_postorder)
            root.right = dfs(right_inorder, right_postorder)
            return root
        
        root = dfs(inorder, postorder)
        return root

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
