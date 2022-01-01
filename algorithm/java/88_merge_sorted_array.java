// Solution 1. allocate a new array to store sorted result.

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] sortedArr = new int[m+n];
        int i = 0;
        int j = 0;
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                sortedArr[i+j] = nums1[i];
                i++;
            } else {
                sortedArr[i+j] = nums2[j];
                j++;
            }
        }
        for (; i < m; i++) {
            sortedArr[i+j] = nums1[i];
        }
        for (; j < n; j++) {
            sortedArr[i+j] = nums2[j];
        }
        for (int k = 0; k < m+n; k++) {
            nums1[k] = sortedArr[k];
        }
        return ;
    }
}


// Solution 2 insert number at the end of nums1 

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1;
        int j = n-1;
        int k = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] >= nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
        for (; i >= 0; i--, k--) {
            nums1[k] = nums1[i];
        }
        for (; j >= 0; j--, k--) {
            nums1[k] = nums2[j];
        }
        return ;
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
