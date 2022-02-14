class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        sum = 0
        current = 0
        for i in range(2,n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current += 1
                sum += current
            else:
                current = 0
        return sum