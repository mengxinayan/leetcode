/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        realSerialize(root, sb);
        return sb.toString();
    }

    public void realSerialize(TreeNode root, StringBuilder sb) {
        if (root != null) {
            sb.append(root.val);
            sb.append(",");
            realSerialize(root.left, sb);
            realSerialize(root.right, sb);
        } else {
            sb.append("null,");
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] dataArr = data.split(",");
        List<String> dataList = new ArrayList<>(Arrays.asList(dataArr));
        // dataList = Arrays.asList(dataArr);
        TreeNode ans = realDeserialize(dataList);
        return ans;
    }

    public TreeNode realDeserialize(List<String> dataList) {
        if (dataList.get(0).equals("null")) {
            dataList.remove(0);
            return null;
        }

        TreeNode root = new TreeNode(Integer.valueOf(dataList.get(0)));
        dataList.remove(0);
        root.left = realDeserialize(dataList);
        root.right = realDeserialize(dataList);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

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
