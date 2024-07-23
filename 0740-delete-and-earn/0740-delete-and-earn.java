class Solution {
    public int deleteAndEarn(int[] nums) {
        Map<Integer, Integer> points = new HashMap<>();
        int maxNum = 0;
        for (int num : nums) {
            points.put(num, points.getOrDefault(num, 0) + num);
            maxNum = Math.max(maxNum, num);
        }

        int[] dp = new int[maxNum + 1];
        dp[0] = points.getOrDefault(0, 0);
        if (maxNum > 0) dp[1] = points.getOrDefault(1, 0);
        for (int i = 2; i <= maxNum; i++)
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + points.getOrDefault(i, 0));
        
        return dp[maxNum];
    }
}