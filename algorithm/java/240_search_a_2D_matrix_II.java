class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowLength = matrix.length;
        int colLength = matrix[0].length;

        if (target < matrix[0][0] || target > matrix[rowLength-1][colLength-1]) {
            return false;
        }

        boolean ans = false;
        for (int i = 0; i < rowLength; i++) {
            if (target < matrix[i][0] || target > matrix[i][colLength-1]) {
                continue;
            } else {
                int left = 0;
                int right = colLength - 1;
                while (left <= right) {
                    int mid = left + (right - left) / 2;
                    if (target < matrix[i][mid]) {
                        right = mid -1;
                    } else if (target > matrix[i][mid]) {
                        left = mid + 1;
                    } else {
                        ans = true;
                        return ans;
                    }
                }
            }
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