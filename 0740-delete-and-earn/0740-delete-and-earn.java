class Solution {
    public int deleteAndEarn(int[] nums) {
        int maxNum = Arrays.stream(nums).max().orElse(0);
    int[] points = new int[maxNum + 1];
    for (int num : nums) {
        points[num] += num;
    }

    int prev1 = 0, prev2 = 0;
    for (int i = 0; i <= maxNum; i++) {
        int curr = Math.max(prev1, prev2 + points[i]);
        prev2 = prev1;
        prev1 = curr;
    }

    return prev1;
    }
}