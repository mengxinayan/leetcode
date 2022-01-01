class Solution {
    public int[] searchRange(int[] nums, int target) {
        int length = nums.length;
        int[] ans = new int[2];
        ans[0] = -1;
        ans[1] = -1;
        if (length == 0) {
            return ans;
        }
        if (length == 1) {
            if (nums[0] == target) {
                ans[0] = 0;
                ans[1] = 0;
            }
            return ans;
        }

        int left = 0;
        int right = length - 1;
        int mid = -1;
        if (nums[0] == target) {
            ans[0] = 0;
        } else {
            while (left <= right) {
                mid = left + (right - left) / 2;
                if (nums[mid] < target) {
                    left = mid + 1;
                } else if (nums[mid] > target) {
                    right = mid - 1;
                } else {
                    if (mid > 0 && nums[mid-1] < target) {
                        ans[0] = mid;
                        break;
                    } else {
                        right = mid - 1;
                    }
                }
            }
        }
        

        left = 0;
        right = length - 1;
        if (nums[length-1] == target) {
            ans[1] = length - 1;
        } else {
            while (left <= right) {
                mid = left + (right - left) / 2;
                if (nums[mid] < target) {
                    left = mid + 1;
                } else if (nums[mid] > target) {
                    right = mid - 1;
                } else {
                    if (mid < length-1 && nums[mid+1] > target) {
                        ans[1] = mid;
                        break;
                    } else {
                        left = mid + 1;
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
