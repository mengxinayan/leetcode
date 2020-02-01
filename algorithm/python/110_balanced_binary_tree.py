# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
平衡二叉树意味着每个树的子树也是一棵平衡二叉树，这是一个递归的定义，向下面这样的树便不是平衡二叉树：
A balanced binary tree means that the subtree of each tree is also a balanced binary tree. This is a recursive definition. A tree like this is not a balanced tree:
      1
     / \
    2   2
   /     \
  3       3
 /         \
4           4
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def cal_depth(root):
            if root == None:
                return 0
            return max( cal_depth(root.left)+1, cal_depth(root.right)+1 )

        if root == None:
            return True
        # 一棵树左子树和右子树高度差大于1，则必然不是平衡二叉树
        # If the height difference between the left subtree and the right subtree of a tree is greater than 1, it must not be a balanced binary tree.
        elif ( root != None ) and \
             ( abs(cal_depth(root.left) - cal_depth(root.right)) > 1 ):
            return False
        # 继续判断该树的左子树和右子树是不是平衡二叉树
        # Determine if the left and right subtrees of the tree are balanced binary trees
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
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