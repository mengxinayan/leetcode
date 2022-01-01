class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length-1; i >= 0; i--) {
            if (i != digits.length - 1) {
                if (digits[i+1] >= 10) {
                    digits[i+1] = digits[i+1] - 10;
                    digits[i] += 1;
                } else {
                    break;
                }
            } else {
                digits[i] += 1;
            }
        }
        if (digits[0] == 10) {
            int[] ans = new int[digits.length+1];
            ans[0] = 1;
            ans[1] = digits[0] - 10;
            for (int i = 2; i < digits.length; i++) {
                ans[i] = digits[i];
            }
            return ans;
        } else {
            return digits;
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
