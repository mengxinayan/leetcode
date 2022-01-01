// Solution 1: HashMap key takes ** sorted string **
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> strGroup = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            if (strGroup.containsKey(sorted) == false) {
                List<String> tmp = new ArrayList<>();
                tmp.add(strs[i]);
                strGroup.put(sorted, tmp);
            } else {
                strGroup.get(sorted).add(strs[i]);
            }
        }
        List<List<String>> ans = new ArrayList<>();
        for (String str : strGroup.keySet()) {
            ans.add(strGroup.get(str));
        }
        return ans;
    }
}


// Solution 2: HashMap key takes ** char index **
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> strGroup = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            String charArray = stringToCharArray(strs[i]);
            if (strGroup.containsKey(charArray) == false) {
                List<String> tmp = new ArrayList<>();
                tmp.add(strs[i]);
                strGroup.put(charArray, tmp);
            } else {
                strGroup.get(charArray).add(strs[i]);
            }
        }
        List<List<String>> ans = new ArrayList<>(strGroup.values());
        return ans;
    }

    private String stringToCharArray(String str) {
        int[] chars = new int[26];
        for (int i = 0; i < str.length(); i++) {
            chars[str.charAt(i) - 'a'] += 1;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] > 0) {
                // 只记录出现次数会误判，示例 ["bdddddddddd","bbbbbbbbbbc"]
                // 因此需要同时记录出现的字母
                sb.append(i + 'a');
                sb.append(chars[i]);
            }
        }
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
