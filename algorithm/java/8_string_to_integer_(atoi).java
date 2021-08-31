// Solution 1: traditional parse string

class Solution {
    public int myAtoi(String s) {
        long ans = 0;
        boolean isPositive = true;
        boolean isStart = false;
        int isOutOfRange = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '-') {
                if (isStart == false) {
                    isPositive = false;
                } else {
                    break;
                }
                isStart = true;
            } else if (s.charAt(i) == '+') {
                if (isStart == true) {
                    break;
                }
                isStart = true;
            } else if (Character.isDigit(s.charAt(i)) == true) {
                if (isStart == false) {
                    isStart = true;
                }
                ans = ans * 10 + Character.digit(s.charAt(i), 10);
                if ((isPositive == false) && (-ans <= Integer.MIN_VALUE)) {
                    isOutOfRange = -1;
                    break;
                } else if (ans > Integer.MAX_VALUE) {
                    isOutOfRange = 1;
                    break;
                }
                else {
                    continue;
                }
            } else {
                if ((isStart == false) && s.charAt(i) == ' ' ) {
                    continue;
                }
                break;
            }
        }
        switch (isOutOfRange) {
            case 1:
                return Integer.MAX_VALUE;
            case -1:
                return Integer.MIN_VALUE;
            default:
                if (isPositive == false) {
                    return (int) -ans;
                } else {
                    return (int) ans;
                }
        }
    }
}


// Solution 2: deterministic finite automaton, DFA

class Solution {
    public int myAtoi(String s) {
        Automation automation = new Automation();
        for (int i = 0; i < s.length(); i++) {
            automation.get(s.charAt(i));
        }
        return (int) (automation.sign * automation.ans);
    }
}

class Automation {
    public int sign = 1;
    public long ans = 0;
    private String state = "start";
    private HashMap<String, String[]> table = new HashMap<String, String[]>();

    public Automation() {
        table.put("start", new String[] {"start", "signed", "in_number", "end"});
        table.put("signed", new String[] {"end", "end", "in_number", "end"});
        table.put("in_number", new String[] {"end", "end", "in_number", "end"});
        table.put("end", new String[] {"end", "end", "end", "end"});
    }

    public void get(char ch) {
        state = table.get(state)[get_col(ch)];
        if ("in_number".equals(state)) {
            ans = ans * 10 + ch - '0';
            ans = (sign == 1) ? Math.min(ans, (long) Integer.MAX_VALUE) : Math.min(ans, - (long) Integer.MIN_VALUE);
        } else if ("signed".equals(state)) {
            sign = (ch == '+') ? 1: -1;
        }
    }

    private int get_col(char ch) {
        if (ch == ' ') {
            return 0;
        } else if ((ch == '+') || (ch == '-')) {
            return 1;
        } else if (Character.isDigit(ch) == true) {
            return 2;
        } else {
            return 3;
        }
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
