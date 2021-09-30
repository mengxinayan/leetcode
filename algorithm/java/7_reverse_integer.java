class Solution {
    public int reverse(int x) {
        if (x == 0) {
            return 0;
        }
        if (x == -2147483648) {
            return 0;
        }
        ArrayList<Integer> numberArr =  new ArrayList<>();
        int sign = 1;
        if (x < 0) {
            x = -x;
            sign = -1;
        }
        while (x != 0) {
            numberArr.add(x % 10);
            x = x / 10;
        }
        StringBuilder sb = new StringBuilder();
        if (sign == -1) {
            sb.append('-');
        }
        for (int number : numberArr) {
            sb.append(number);
        }
        String numStr = sb.toString();
        String maxIntStr = Integer.toString(Integer.MAX_VALUE);
        String minIntStr = Integer.toString(Integer.MIN_VALUE);
        if ((sign == 1) && (numStr.length() == maxIntStr.length()) && (numStr.compareTo(maxIntStr) > 0)) {
            return 0;
        } else if ((sign == -1) && (numStr.length() == minIntStr.length()) && (numStr.compareTo(minIntStr) > 0)) {
            return 0;
        } else {
            return Integer.parseInt(numStr);
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
