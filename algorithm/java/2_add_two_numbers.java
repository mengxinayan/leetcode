/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode curr1 = l1;
        ListNode curr2 = l2;
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        int lastVal = 0;
        while ((curr1 != null) || (curr2 != null)) {
            int tmpVal;
            if (curr1 == null) {
                tmpVal = curr2.val;
                curr2 = curr2.next;
            } else if (curr2 == null) {
                tmpVal = curr1.val;
                curr1 = curr1.next;
            } else {
                tmpVal = curr1.val + curr2.val;
                curr1 = curr1.next;
                curr2 = curr2.next;
            }
            
            int sum = lastVal + tmpVal;
            if (sum >= 10) {
                curr.next = new ListNode(sum % 10);
                lastVal = 1;
            } else {
                curr.next = new ListNode(sum);
                lastVal = 0;
            }
            curr = curr.next;
        }

        if (lastVal == 1) {
            curr.next = new ListNode(lastVal);
        }

        return dummy.next;
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
