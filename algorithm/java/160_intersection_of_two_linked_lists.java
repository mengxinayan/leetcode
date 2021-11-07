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
