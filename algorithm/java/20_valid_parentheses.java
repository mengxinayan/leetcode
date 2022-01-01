class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new LinkedList<>();
        boolean ans = true;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == ')') {
                if ((stack.size() == 0) || (stack.peek() != '(')) {
                    ans = false;
                    break;
                } else {
                    stack.pop();
                }
            } else if (ch == ']') {
                if ((stack.size() == 0) || (stack.peek() != '[')) {
                    ans = false;
                    break;
                } else {
                    stack.pop();
                }
            } else if (ch == '}') {
                if ((stack.size() == 0) || (stack.peek() != '{')) {
                    ans = false;
                    break;
                } else {
                    stack.pop();
                }
            } else {
                stack.push(ch);
            }
        }
        if (stack.size() != 0) {
            ans = false;
        }
        return ans;
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
