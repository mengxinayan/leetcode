# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def dfs(preorder: List[int], inorder: List[int]):
            if (len(preorder) == 0) or (len(inorder) == 0):
                return None
            if (len(preorder) == 1) and (len(inorder) == 1):
                return TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            left_inorder = inorder[:index]
            left_preorder = preorder[1:1+len(left_inorder)]
            right_inorder = inorder[index+1:]
            right_preorder = preorder[1+len(left_inorder):]
            root = TreeNode(preorder[0])
            root.left = dfs(left_preorder, left_inorder)
            root.right = dfs(right_preorder, right_inorder)
            return root
        
        root = dfs(preorder, inorder)
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
