class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE) {
            if (divisor == -1) {
                return Integer.MAX_VALUE;
            }
        }
        if (divisor == 1) {
            return dividend;
        }
        if (divisor == -1) {
            return -dividend;
        }

        boolean sign = true;
        if (dividend > 0) {
            dividend = -dividend;
            sign = !sign;
        }
        if (divisor > 0) {
            divisor = -divisor;
            sign = !sign;
        }

        int left = 1, right = Integer.MAX_VALUE;
        int ans = 0;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            boolean check = quickAdd(divisor, mid, dividend);
            if (check) {
                ans = mid;
                if (mid == Integer.MAX_VALUE) {
                    break;
                }
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return sign? ans : -ans;
    }

    public boolean quickAdd(int divisor, int mid, int dividend) {
        // if a*b <= c meets, then return true.
        int result = 0;
        int add = divisor;
        while (mid != 0) {    
            if ((mid & 1) != 0) {
                if (result < dividend - add) {
                    return false;
                }
                result += add;
            }     
            if (mid != 1) {
                if (add < dividend - add) {
                    return false;
                }
                add += add;
            }
            mid = mid >> 1;
        }
        return true;
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
