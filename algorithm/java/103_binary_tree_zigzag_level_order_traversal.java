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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        int count = 1;
        queue.offer(root);
        while (!queue.isEmpty()) {
            int length = queue.size();
            List<Integer> tmpArr = new ArrayList<>();
            for (int i = 0; i < length; i++) {
                TreeNode tmpNode = queue.poll();
                if (tmpNode != null) {
                    tmpArr.add(tmpNode.val);
                    queue.offer(tmpNode.left);
                    queue.offer(tmpNode.right);
                }
            }
            if (!tmpArr.isEmpty()) {
                if (count % 2 == 0) {
                    Collections.reverse(tmpArr);
                }
                ans.add(tmpArr);
            }
            count++;
        }
        return ans;
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
