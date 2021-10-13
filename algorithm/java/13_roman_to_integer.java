class Solution {
    public int romanToInt(String s) {
        int i = 0;
        int ans = 0;
        while (i != s.length()) {
            char ch = s.charAt(i);
            switch(ch) {
                case 'I': {
                    if (i+1 != s.length() && s.charAt(i+1) == 'V') {
                        ans += 4;
                        i++;
                    } else if (i+1 != s.length() && s.charAt(i+1) == 'X') {
                        ans += 9;
                        i++;
                    } else {
                        ans += 1;
                    }
                    break;
                }
                case 'X': {
                    if (i+1 != s.length() && s.charAt(i+1) == 'L') {
                        ans += 40;
                        i++;
                    } else if (i+1 != s.length() && s.charAt(i+1) == 'C') {
                        ans += 90;
                        i++;
                    } else {
                        ans += 10;
                    }
                    break;
                }
                case 'C': {
                    if (i+1 != s.length() && s.charAt(i+1) == 'D') {
                        ans += 400;
                        i++;
                    } else if (i+1 != s.length() && s.charAt(i+1) == 'M') {
                        ans += 900;
                        i++;
                    } else {
                        ans += 100;
                    }
                    break;
                }
                case 'V': {
                    ans += 5;
                    break;
                }
                case 'L': {
                    ans += 50;
                    break;
                }
                case 'D': {
                    ans += 500;
                    break;
                }
                case 'M': {
                    ans += 1000;
                    break;
                }
            }
            i++;
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
