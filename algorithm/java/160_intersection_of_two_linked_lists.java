/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

// Solution 1: Use HashSet
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashSet<ListNode> nodeSet = new HashSet<>();
        ListNode curr = headA;
        while (curr != null) {
            nodeSet.add(curr);
            curr = curr.next;
        }
        curr = headB;
        while (curr != null) {
            if (nodeSet.contains(curr)) {
                break;
            } else {
                curr = curr.next;
            }
        }
        return curr;
    }
}


// Solution 2: Two Pointers
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        ListNode curr1 = headA;
        ListNode curr2 = headB;
        while (curr1 != curr2) {
            curr1 = (curr1 == null) ? headB : curr1.next;
            curr2 = (curr2 == null) ? headA : curr2.next;
        }
        return curr1;
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
