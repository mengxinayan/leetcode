// Solution 1: My own solution

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, HashSet<Integer>> numIndexMap = new HashMap<Integer, HashSet<Integer>>();
        for (int i = 0; i < nums.length; i++) {
            Integer num = nums[i];
            if (numIndexMap.containsKey(num) == false) {
                numIndexMap.put(num, new HashSet<Integer>());
                numIndexMap.get(num).add(i);
            } else {
                numIndexMap.get(num).add(i);
            }
        }
        int[] ans = new int[2];
        int index = 0;
        for (Integer key: numIndexMap.keySet()) {
            Integer goalKey = target - key;
            if (goalKey.equals(key) == true) {
                if (numIndexMap.get(goalKey).size() > 1) {
                    for (Integer temp: numIndexMap.get(goalKey)) {
                        ans[index] = temp;
                        index += 1;
                    }
                }
            } else {
                if (numIndexMap.containsKey(goalKey) == true) {
                    for (Integer temp: numIndexMap.get(key)) {
                        ans[0] = temp;
                    }
                    for (Integer temp: numIndexMap.get(goalKey)) {
                        ans[1] = temp;
                    }
                }
            }
        }
        return ans;
    }
}

// Solution 2: Official solution

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numIndexMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (numIndexMap.containsKey(target - nums[i])) {
                return new int[]{numIndexMap.get(target - nums[i]), i};
            } else {
                numIndexMap.put(nums[i], i);
            }
        }
        return new int[2];
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
