class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                nums = [i, seen[complement]]
                nums.sort()
                return nums
            seen[nums[i]] = i