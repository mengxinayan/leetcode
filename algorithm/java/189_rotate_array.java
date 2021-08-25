// Solution 1: My own solution

class Solution {
    public void rotate(int[] nums, int k) {
        if (nums.length <= 1) {
            return ;
        }

        int start = nums.length - k % nums.length;
        if (start == nums.length) {
            return ;
        }

        int[] temp = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            temp[i] = nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = temp[start];
            start = (start + 1) % nums.length;
        }
    }
}


// Solution 2: official solution 1

class Solution {
    public void rotate(int[] nums, int k) {
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            ans[(i+k) % nums.length] = nums[i];
        }
        System.arraycopy(ans, 0, nums, 0, nums.length);
    }
}


// Solution 3: official solution 3

class Solution {
    private void reverse(int[] nums, int start, int end) {
        int temp = 0;
        while (start < end) {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    public void rotate(int[] nums, int k) {
        reverse(nums, 0, nums.length-1);
        reverse(nums, 0, k % nums.length -1);
        reverse(nums, k % nums.length, nums.length-1);
    }
}
