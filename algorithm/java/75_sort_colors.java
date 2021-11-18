// Solution 1
class Solution {
    public void sortColors(int[] nums) {
        int index = 0;
        while (index < nums.length && nums[index] == 0) {
            index++;
        }
        for (int i = index; i < nums.length; i++) { // swap all 0 at the begin
            if (nums[i] == 0) {
                int tmp = nums[index];
                nums[index] = nums[i];
                nums[i] = tmp;
                index++;
            }
        }
        for (int i = index; i < nums.length; i++) { // swap all 1 after the 0
            if (nums[i] == 1) {
                int tmp = nums[index];
                nums[index] = nums[i];
                nums[i] = tmp;
                index++;
            }
        }
        return ;
    }
}


// Solution 2
class Solution {
    public void sortColors(int[] nums) {
        int p0 = 0;
        int p2 = nums.length - 1;
        for (int i = 0; i < nums.length; i++) {
            while (i < p2 && nums[i] == 2) {
                int tmp = nums[p2];
                nums[p2] = nums[i];
                nums[i] = tmp;
                p2--;
            }
            if (nums[i] == 0) {
                int tmp = nums[p0];
                nums[p0] = nums[i];
                nums[i] = tmp;
                p0++;
            }
        }
        return ;
    }
}


// Solution 3
class Solution {
    public void sortColors(int[] nums) {
        int p0 = 0;
        int p1 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                int tmp = nums[p1];
                nums[p1] = nums[i];
                nums[i] = tmp;
                p1++;
            }
            if (nums[i] == 0) {
                int tmp = nums[p0];
                nums[p0] = nums[i];
                nums[i] = tmp;
                if (p0 < p1) {
                    tmp = nums[p1];
                    nums[p1] = nums[i];
                    nums[i] = tmp;
                }
                p0++;
                p1++;
            }
        }
        return ;
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
