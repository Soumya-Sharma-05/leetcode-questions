class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total_sum = n * (n + 1) // 2
        array_sum = sum(nums)
        return total_sum - array_sum
        
