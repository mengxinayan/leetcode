# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def dfs_build_tree(arr: List[int]):
            if len(arr) == 0:
                return None
            elif len(arr) == 1:
                return TreeNode(arr[0])
            else:
                mid = len(arr) // 2
                left_arr = arr[:mid]
                right_arr = arr[mid+1:]
                root = TreeNode(arr[mid])
                root.left = dfs_build_tree(left_arr)
                root.right = dfs_build_tree(right_arr)
                return root

        arr = []
        tmp = head
        while tmp != None:
            arr.append(tmp.val)
            tmp = tmp.next
        root = dfs_build_tree(arr)
        return root

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
