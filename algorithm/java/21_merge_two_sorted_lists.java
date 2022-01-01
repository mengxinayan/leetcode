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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        }
        ListNode dummy = new ListNode();
        ListNode tmp = dummy;
        ListNode tmp1 = l1;
        ListNode tmp2 = l2;
        while ((tmp1 != null) && (tmp2 != null)) {
            if (tmp1.val < tmp2.val) {
                tmp.next = new ListNode(tmp1.val);
                tmp = tmp.next;
                tmp1 = tmp1.next;
            } else if (tmp1.val > tmp2.val) {
                tmp.next = new ListNode(tmp2.val);
                tmp = tmp.next;
                tmp2 = tmp2.next;
            } else {
                tmp.next = new ListNode(tmp1.val);
                tmp = tmp.next;
                tmp1 = tmp1.next;
                tmp.next = new ListNode(tmp2.val);
                tmp = tmp.next;
                tmp2 = tmp2.next;
            }
        }
        if ((tmp1 != null) && (tmp2 == null)) {
            tmp.next = tmp1;
        } else if ((tmp1 == null) && (tmp2 != null)) {
            tmp.next = tmp2;
        } else {
            tmp.next = null;
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
