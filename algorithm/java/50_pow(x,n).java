class Solution {
    public double myPow(double x, int n) {
        if (x == 0 || x == 1) {
            return x;
        }
        if (n > 0) {
            return calPow(x, n);
        } else if (n < 0) {
            return calPow(1/x, -n);
        } else {
            return 1;
        }
    }

    // use long type: because abs(Integer.MIN_VALUE) > abs(Integer.MAX_VALUE)
    public double calPow(double x, long n) {
        if (n == 0) {
            return 1;
        }
        double tmp = calPow(x, n/2);
        if (n % 2 == 0) {
            return tmp * tmp;
        } else {
            return tmp * tmp * x;
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
