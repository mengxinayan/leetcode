class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> nonRepeatingChIndexMap = new HashMap<Character, Integer>();
        HashSet<Character> repeatingChSet = new HashSet<Character>();
        for (int i = 0; i < s.length(); i++) {
            Character ch = s.charAt(i);
            if (repeatingChSet.contains(ch) == false) {
                if (nonRepeatingChIndexMap.containsKey(ch) == false) {
                    nonRepeatingChIndexMap.put(ch, i);
                } else {
                    nonRepeatingChIndexMap.remove(ch);
                    repeatingChSet.add(ch);
                }
            }
        }
        if (nonRepeatingChIndexMap.values().isEmpty() == true) {
            return -1;
        } else {
            return Collections.min(nonRepeatingChIndexMap.values());
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
