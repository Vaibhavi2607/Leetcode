class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            temp = 0
            mpp = {}
            for num in nums:
                mpp[num] = mpp.get(num, 0) + 1
                if mpp[num] == 2:
                    temp += 1

            if temp == 0:
                break
            nums = nums[min(3, len(nums)):]
            count += 1
        return count
        