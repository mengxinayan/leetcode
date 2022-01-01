// Solution 1: BFS

class Solution {
    public int numIslands(char[][] grid) {
        int ans = 0;
        int rowLength = grid.length;
        int colLength = grid[0].length;
        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < colLength; j++) {
                if (grid[i][j] == '1') {
                    ans += 1;
                    Queue<Integer> queue = new LinkedList<>();
                    queue.offer(i * colLength + j);
                    while (!queue.isEmpty()) {
                        int tmp = queue.poll();
                        int row = tmp / colLength;
                        int col = tmp % colLength;
                        if ((row - 1 >= 0) && (grid[row-1][col] == '1')) {
                            grid[row-1][col] = '-';
                            queue.offer((row-1) * colLength + col);
                        }
                        if ((row + 1 < rowLength) && (grid[row+1][col] == '1')) {
                            grid[row+1][col] = '-';
                            queue.offer((row+1) * colLength + col);
                        }
                        if ((col - 1 >= 0) && (grid[row][col-1] == '1')) {
                            grid[row][col-1] = '-';
                            queue.offer(row * colLength + col - 1);
                        }
                        if ((col + 1 < colLength) && (grid[row][col+1] == '1')) {
                            grid[row][col+1] = '-';
                            queue.offer(row * colLength + col + 1);
                        }
                    }
                }
            }
        }
        return ans;   
    }
}


// Solution 2: DFS

class Solution {
    public int numIslands(char[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    ans++;
                    dfs(i, j, grid);
                }
            }
        }
        return ans;
    }

    public void dfs(int row, int col, char[][] grid) {
        if ((row < 0) || (row >= grid.length) || (col < 0) || (col >= grid[0].length) || (grid[row][col] != '1')) {
            return ;
        }

        grid[row][col] = '-';
        dfs(row-1, col, grid);
        dfs(row+1, col, grid);
        dfs(row, col-1, grid);
        dfs(row, col+1, grid);
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
