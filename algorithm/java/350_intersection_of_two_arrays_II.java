// Solution 1: use hash table

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> hashTable1 = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> hashTable2 = new HashMap<Integer, Integer>();

        for (int numInt: nums1) {
            Integer num = Integer.valueOf(numInt);
            if (hashTable1.containsKey(num) == false) {
                hashTable1.put(num, 1);
            } else {
                hashTable1.put(num, hashTable1.get(num) + 1);
            }
        }
        for (int numInt: nums2) {
            Integer num = Integer.valueOf(numInt);
            if (hashTable2.containsKey(num) == false) {
                hashTable2.put(num, 1);
            } else {
                hashTable2.put(num, hashTable2.get(num) + 1);
            }
        }

        ArrayList<Integer> ansArray = new ArrayList<Integer>();
        for (Integer key: hashTable1.keySet()) {
            if (hashTable2.containsKey(key) == true) {
                int times = hashTable1.get(key) <= hashTable2.get(key)? hashTable1.get(key): hashTable2.get(key);
                for (int i = 0; i < times; i++) {
                    ansArray.add(key);
                }
            }
        }

        int[] ans = new int[ansArray.size()];
        for (int i = 0; i < ansArray.size(); i++) {
            ans[i] = ansArray.get(i).intValue();
        }
        return ans;
    }
}

// Solution 2: use two pointers with sorted array

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        ArrayList<Integer> ansArray = new ArrayList<Integer>();
        for (int i = 0, j = 0; (i < nums1.length) && (j < nums2.length);) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                ansArray.add(Integer.valueOf(nums1[i]));
                i++;
                j++;
            }
        }

        int[] ans = new int[ansArray.size()];
        for (int i = 0; i < ansArray.size(); i++) {
            ans[i] = ansArray.get(i).intValue();
        }
        return ans;
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
