class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<>();

        if (digits.equals("") == true) {
            return ans;
        }
        Map<Character, String> map = new HashMap<>();
        map.put('2', new String("abc"));
        map.put('3', new String("def"));
        map.put('4', new String("ghi"));
        map.put('5', new String("jkl"));
        map.put('6', new String("mno"));
        map.put('7', new String("pqrs"));
        map.put('8', new String("tuv"));
        map.put('9', new String("wxyz"));

        backtracing(new StringBuilder(), ans, 0, digits, map);
        return ans;
    }

    public void backtracing(StringBuilder sb, List<String> ans, int index, String digits, Map<Character, String> map) {
        if (index == digits.length()) {
            ans.add(sb.toString());
        } else {
            String tmp = map.get(digits.charAt(index));
            for (int i = 0; i < tmp.length(); i++) {
                sb.append(tmp.charAt(i));
                backtracing(sb, ans, index+1, digits, map);
                sb.deleteCharAt(index);
            }
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
