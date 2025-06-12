class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int n = nums.length;
        int max_element = Math.abs(nums[0] - nums[n-1]);
        for(int i = 0; i < n-1; i++){
            max_element = Math.max(max_element, Math.abs(nums[i] - nums[i+1]));
        }
        return max_element;
    }
}