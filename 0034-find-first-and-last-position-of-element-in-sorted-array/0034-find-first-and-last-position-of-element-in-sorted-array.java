class Solution {
    public int[] searchRange(int[] nums, int target) {
        int i=-1, j=-1;
        for (int n=0; n<nums.length; n++){
            if(nums[n] == target){
                if(i==-1){
                    i = n;
                }
                j = n;
            }
        }
        return new int[]{i,j};
    }
}