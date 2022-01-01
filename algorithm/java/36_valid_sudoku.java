class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[][] rowArr = new int[9][9];
        int[][] colArr = new int[9][9];
        int[][] boxArr = new int[9][9];
        boolean ans = true;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '0' - 1;
                    int boxNumber = (i / 3) * 3 + (j / 3);
                    if ((rowArr[i][num] != 0) || (colArr[j][num] != 0) || (boxArr[boxNumber][num] != 0)) {
                        ans = false;
                        break;
                    }
                    rowArr[i][num] = 1;
                    colArr[j][num] = 1;
                    boxArr[boxNumber][num] = 1;
                }
            }
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
