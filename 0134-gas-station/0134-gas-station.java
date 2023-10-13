class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int diff=0;
        for(int i=0;i<gas.length;i++){
            diff+=gas[i]-cost[i];
        }

        if(diff<0) return -1;


        int tank=0;
        int res=0;
        for(int i=0;i<gas.length;i++){
            tank+=gas[i]-cost[i];

            if(tank<0){
                res=i+1;
                tank=0;
            }
        }
        return res;
    }
}