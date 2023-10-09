class Solution {
    public void moveZeroes(int[] nums) {
        int i=0;
        for(int n=0; n<nums.length; n++){
            if(nums[n] != 0){
                if( n != i){
                    int temp =nums[i];
                    nums[i] = nums[n];
                    nums[n] = temp;
                }
                i++;
            }
        }
    }
}