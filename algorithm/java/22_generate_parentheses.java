class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        backtracking(new StringBuilder(), 0, 0, n, ans);
        return ans;
    }

    public void backtracking(StringBuilder sb, int left, int right, int n, List<String> ans) {
        if (left+right == 2*n) {
            ans.add(sb.toString());
        }
        if (left < n) {
            sb.append('(');
            backtracking(sb, left+1, right, n, ans);
            sb.deleteCharAt(sb.length() - 1);
        }
        if (right < left) {
            sb.append(')');
            backtracking(sb, left, right+1, n, ans);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}


/**
 * This is my personal record of solving Leetcode Problems. 
 * If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
 * Copyright (C) 2020-2022  mengxinayan
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
