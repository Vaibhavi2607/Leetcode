class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        # Step 1: Calculate base sum of numbers 
        base_sum = sum(nums)
        # Step 2: Calculate the gains for XOR of each number
        gains = [(num ^ k) - num for num in nums]
        # Step 3: Sort the  gains descendingly
        gains.sort(reverse=True)
        # Step 4: Choose best even-number gains sum
        max_gain = 0
        current_gain = 0
        count = 0
        for gain in gains:
            current_gain += gain
            count += 1
            # Step 5: Only consider even count of XORs
            if count % 2 == 0:
                max_gain = max(max_gain, current_gain)
        return base_sum + max_gain