class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int low = 0;
        int high = n-1;
        int count = 0;
        while(low<high){
            int temp = nums[low]+nums[high];
            if(temp == k){
                low++;
                high--;
                count++;
            }else if(temp<k){
                low++;
            }else
                high--;
        }
        return count;
    }
}