class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtracking(0, tmp, ans, used, nums);
        return ans;
    }

    public void backtracking(int start, List<Integer> tmp, List<List<Integer>> ans, boolean[] used, int[] nums) {
        ans.add(new ArrayList<>(tmp));
        for (int i = start; i < nums.length; i++) {
            if (used[i] == false) {
                used[i] = true;
                tmp.add(nums[i]);
                backtracking(i+1, tmp, ans, used, nums);
                tmp.remove(tmp.size() - 1);
                used[i] = false;
            }
        }
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
