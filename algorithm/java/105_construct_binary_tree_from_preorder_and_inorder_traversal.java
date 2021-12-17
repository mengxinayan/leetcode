/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private Map<Integer, Integer> indexMap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            indexMap.put(inorder[i], i);
        }
        TreeNode root = realBuildTree(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1);
        return root;
    }

    public TreeNode realBuildTree(int[] preorder, int pre_left, int pre_right,
                    int[] inorder, int in_left, int in_right) {
        if (pre_left > pre_right) {
            return null;
        }

        int rootVal = preorder[pre_left];
        int rootIndex = indexMap.get(rootVal);

        TreeNode root = new TreeNode(rootVal);
        int leftTreeLength = rootIndex - in_left;

        root.left = realBuildTree(preorder, pre_left+1, pre_left+leftTreeLength, inorder, in_left, rootIndex-1);
        root.right = realBuildTree(preorder, pre_left+leftTreeLength+1, pre_right, inorder, rootIndex+1, in_right);

        return root;
    }
}

/**
 * This is my personal record of solving Leetcode Problems. 
 * If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
 * Copyright (C) 2020-2021  mengxinayan
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
