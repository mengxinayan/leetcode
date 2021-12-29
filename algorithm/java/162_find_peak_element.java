class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1) {
            return 0;
        }
        if (nums.length == 2) {
            return nums[0] > nums[1]? 0: 1;
        }

        int length = nums.length;
        float[] arr = new float[length+2];
        arr[0] = Float.NEGATIVE_INFINITY;
        for (int i = 0; i < length; i++) {
            arr[i+1] = nums[i];
        }
        arr[length+1] = Float.NEGATIVE_INFINITY;

        int ans = binarySearchPeak(arr, 1, length) - 1;
        return ans;
    }

    public int binarySearchPeak(float[] arr, int left, int right) {
        if (left > right) {
            return 0;
        }
        if (left == right) {
            return left;
        }

        int mid = left + (right - left) / 2;
        int ans = 0;
        if (arr[mid] > arr[mid-1] && arr[mid] > arr[mid+1]) {
            ans = mid;
        }
        int leftAns = binarySearchPeak(arr, left, mid-1);
        int rightAns = binarySearchPeak(arr, mid+1, right);
        if (arr[ans] < arr[leftAns]) {
            ans = leftAns;
        } if (arr[ans] < arr[rightAns]) {
            ans = rightAns;
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
