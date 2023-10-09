class Solution {
    public int jump(int[] nums) {
        int reach = 0;
        int jump = 0;
        int last = 0;
        for(int i=0; i<nums.length-1; i++){
            last = Math.max(last,i+nums[i]);
            if(i==reach){
                reach = last;
                jump++;
            }
        }
        return jump;
    }
}