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

// Solution 1: use an array to store value, then check it whether is palindrome

class Solution {
    public boolean isPalindrome(ListNode head) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (ListNode tmp = head; tmp != null; tmp = tmp.next) {
            arr.add(tmp.val);
        }
        boolean ans = true;
        for (int left = 0, right = arr.size()-1; left < right; left++, right--) {
            if (arr.get(left) != arr.get(right)) {
                ans = false;
                break;
            }
        }
        return ans;
    }
}


// Solution 2: fast-slow pointer, then reverse second half Linked list, finally check it whether is palindrome.

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode firstHalfEnd = slow;
        ListNode secondHalfReverse = reverseListNode(firstHalfEnd.next);
        boolean ans = true;
        for (ListNode tmpFirst = head, tmpSecond = secondHalfReverse;
            (tmpFirst != null) && (tmpSecond != null);
            tmpFirst = tmpFirst.next, tmpSecond = tmpSecond.next) {
                if (tmpFirst.val != tmpSecond.val) {
                    ans = false;
                    break;
                }
            }

        firstHalfEnd.next = reverseListNode(secondHalfReverse);
        return ans;
    }

    private ListNode reverseListNode(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode curr = head;
        ListNode prev = null;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
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
