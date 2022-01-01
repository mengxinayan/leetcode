// Solution 1: My own solution

class Solution {
    public void rotate(int[] nums, int k) {
        if (nums.length <= 1) {
            return ;
        }

        int start = nums.length - k % nums.length;
        if (start == nums.length) {
            return ;
        }

        int[] temp = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            temp[i] = nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = temp[start];
            start = (start + 1) % nums.length;
        }
    }
}


// Solution 2: official solution 1

class Solution {
    public void rotate(int[] nums, int k) {
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            ans[(i+k) % nums.length] = nums[i];
        }
        System.arraycopy(ans, 0, nums, 0, nums.length);
    }
}


// Solution 3: official solution 3

class Solution {
    private void reverse(int[] nums, int start, int end) {
        int temp = 0;
        while (start < end) {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    public void rotate(int[] nums, int k) {
        reverse(nums, 0, nums.length-1);
        reverse(nums, 0, k % nums.length -1);
        reverse(nums, k % nums.length, nums.length-1);
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
