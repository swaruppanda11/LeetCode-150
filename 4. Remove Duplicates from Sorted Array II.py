class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 0
        while r < len(nums):
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1
            
            for i in range(2, count):
                nums[l] = nums[r]:
                l += 1
            r += 1
        return l