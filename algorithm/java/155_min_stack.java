class MinStack {
    private Deque<Integer> stack;
    private int minValue;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new LinkedList<>();
        minValue = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        stack.push(val);
        if (val < minValue) {
            minValue = val;
        }
    }
    
    public void pop() {
        int topValue = stack.pop();
        if (topValue == minValue) {
            minValue = Integer.MAX_VALUE;
            for (int num: stack) {
                minValue = Math.min(minValue, num);
            }
        }
    }
    
    public int top() {
        int ans = stack.peek();
        return ans;
    }
    
    public int getMin() {
        return minValue;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

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
