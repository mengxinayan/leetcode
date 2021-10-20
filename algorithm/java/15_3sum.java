class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<List<Integer>> ansSet = new HashSet<>();
        HashMap<Integer, Integer> numCount = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (numCount.containsKey(nums[i]) == false) {
                numCount.put(nums[i], 1);
            } else {
                numCount.put(nums[i], numCount.get(nums[i]) + 1);
            }
        }
        for (int i = 0; i < nums.length - 1; i++) {
            numCount.put(nums[i], numCount.get(nums[i]) - 1);
            for (int j = i + 1; j < nums.length; j++) {
                int anotherNum = 0 - nums[i] - nums[j];
                
                numCount.put(nums[j], numCount.get(nums[j]) - 1);
                if (numCount.containsKey(anotherNum) && numCount.get(anotherNum) > 0) {
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(nums[i]);
                    tmp.add(nums[j]);
                    tmp.add(anotherNum);
                    Collections.sort(tmp);
                    ansSet.add(tmp);
                }
                numCount.put(nums[j], numCount.get(nums[j]) + 1);
            }
            numCount.put(nums[i], numCount.get(nums[i]) + 1);
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (List<Integer> tmp : ansSet) {
            ans.add(tmp);
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
