class Solution {
    public String countAndSay(int n) {
        String ans = "1";
        for (int i = 1; i < n; i++) {
            ans = sayNumber(ans);
        }
        return ans;
    }

    static String sayNumber(String num) {
        StringBuilder sb = new StringBuilder();
        char prevCh = num.charAt(0);
        int count = 1;
        for (int i = 1; i < num.length(); i++) {
            if (num.charAt(i) != prevCh) {
                sb.append(String.valueOf(count));
                sb.append(String.valueOf(prevCh));
                prevCh = num.charAt(i);
                count = 1;
            } else {
                count++;
            }
        }
        sb.append(String.valueOf(count));
        sb.append(String.valueOf(prevCh));
        return sb.toString();
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
