# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        def dfs(root: TreeNode, tmp_arr: List[int]):
            if (root.left == None) and (root.right == None):
                if sum(tmp_arr) == targetSum:
                    ans.append(tmp_arr[:])
            else:
                if root.left != None:
                    dfs(root.left, tmp_arr+[root.left.val])
                if root.right != None:
                    dfs(root.right, tmp_arr+[root.right.val])
            tmp_arr.pop()

        if root == None:
            return []
        ans = []
        dfs(root, [root.val])
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
