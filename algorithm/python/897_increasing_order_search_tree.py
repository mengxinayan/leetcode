# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def in_order_traversal(root: TreeNode):
            if root != None:
                in_order_traversal(root.left)
                self.arr.append(root.val)
                in_order_traversal(root.right)
        
        def make_tree(nums: List[int]) -> TreeNode:
            ans = curr = TreeNode(nums[0])
            for i in range(1, len(nums)):
                curr.left = None
                curr.right = TreeNode(nums[i])
                curr = curr.right
            return ans

        self.arr = []
        in_order_traversal(root)
        ans = make_tree(self.arr)
        return ans

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
