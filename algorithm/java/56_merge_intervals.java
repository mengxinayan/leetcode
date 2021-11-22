class Solution {
    public int[][] merge(int[][] intervals) {
        /**
         * Custom Sort, rule is as bellow:
         * intervals[][0]: From small to big
         * if interval[i][0] == interval[j][1], then intervals[][1]: From big to small
         */
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] < o2[0]) {
                    return -1;
                } else if (o1[0] > o2[0]) {
                    return 1;
                } else {
                    if (o1[1] < o2[1]) {
                        return 1;
                    } else if (o1[1] > o2[1]) {
                        return -1;
                    } else {
                        return 0;
                    }
                }
            }
        });
        int startVal = -1;
        int endVal = -1;
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++) {
            if (startVal != intervals[i][0]) {
                if (intervals[i][0] <= endVal) {
                    endVal = intervals[i][1] > endVal? intervals[i][1] : endVal;
                } else {
                    int[] tmp = {startVal, endVal};
                    list.add(tmp);
                    startVal = intervals[i][0];
                    endVal = intervals[i][1];
                }
            } else {
                continue;
            }
        }

        // Add last pair and remove first pair ([-1, -1])
        int[] tmp = {startVal, endVal};
        list.add(tmp);
        list.remove(0);

        int[][] ans = new int[list.size()][2];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = list.get(i);
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
