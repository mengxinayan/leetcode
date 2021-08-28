class Solution {
    public int myAtoi(String s) {
        long ans = 0;
        boolean isPositive = true;
        boolean isStart = false;
        int isOutOfRange = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '-') {
                if (isStart == false) {
                    isPositive = false;
                } else {
                    break;
                }
                isStart = true;
            } else if (s.charAt(i) == '+') {
                if (isStart == true) {
                    break;
                }
                isStart = true;
            } else if (Character.isDigit(s.charAt(i)) == true) {
                if (isStart == false) {
                    isStart = true;
                }
                ans = ans * 10 + Character.digit(s.charAt(i), 10);
                if ((isPositive == false) && (-ans <= Integer.MIN_VALUE)) {
                    isOutOfRange = -1;
                    break;
                } else if (ans > Integer.MAX_VALUE) {
                    isOutOfRange = 1;
                    break;
                }
                else {
                    continue;
                }
            } else {
                if ((isStart == false) && s.charAt(i) == ' ' ) {
                    continue;
                }
                break;
            }
        }
        switch (isOutOfRange) {
            case 1:
                return Integer.MAX_VALUE;
            case -1:
                return Integer.MIN_VALUE;
            default:
                if (isPositive == false) {
                    return (int) -ans;
                } else {
                    return (int) ans;
                }
        }
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
