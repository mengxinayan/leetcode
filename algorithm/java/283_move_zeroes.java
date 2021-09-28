// Solution 1: record zero index.
class Solution {
    public void moveZeroes(int[] nums) {
        ArrayList<Integer> nonZeroArray = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nonZeroArray.add(nums[i]);
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (i < nonZeroArray.size()){
                nums[i] = nonZeroArray.get(i);
            } else {
                nums[i] = 0;
            }
        }
        return ;
    }
}


// Two pointers.
/**
 * There are two pointers, left pointer and right pointer.
 * From 0 to left pointer, all numbers are non-zero.
 * From left to right pointer(that is end), all number are zero.
 */
class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0;
        int right = 0;
        while (right < nums.length) {
            if (nums[right] != 0) {
                int tmp = nums[right];
                nums[right] = nums[left];
                nums[left] = tmp;
                left++;
            }
            right++;
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
