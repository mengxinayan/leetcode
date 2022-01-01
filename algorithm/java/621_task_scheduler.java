class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < tasks.length; i++) {
            if (map.containsKey(tasks[i]) == false) {
                map.put(tasks[i], 1);
            } else {
                map.put(tasks[i], map.get(tasks[i])+1);
            }
        }

        PriorityQueue<CharCount> pq = new PriorityQueue<>();
        for (Character ch : map.keySet()) {
            pq.offer(new CharCount(ch, map.get(ch)));
        }

        int ans = 0;
        int taskNumber = tasks.length;
        List<CharCount> charCountArr = new ArrayList<>();
        while (taskNumber != 0) {
            charCountArr.clear();
            for (int i = 0; i <= n; i++) {
                if (pq.size() > 0) {
                    CharCount tmp = pq.poll();
                    tmp.count--;
                    if (tmp.count != 0) {
                        charCountArr.add(tmp);
                    }
                    taskNumber--;
                    ans++;
                } else {
                    if (charCountArr.isEmpty()) {
                        break;
                    } else {
                        ans++;
                    }
                }
            }
            for (CharCount tmp : charCountArr) {
                pq.offer(tmp);
            }
        }
        return ans;
    }
}

class CharCount implements Comparable<CharCount> {
    public char ch;
    public int count;

    public CharCount(char ch, int count) {
        this.ch = ch;
        this.count = count;
    }

    @Override
    public int compareTo(CharCount o) {
        if (count == o.count) {
            return ch - o.ch;
        } else {
            // From big to small
            return o.count - count;
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
