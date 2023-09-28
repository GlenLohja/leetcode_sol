class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        
        # if k > len(nums):
        #     k = len(nums) + (k % len(nums))
        # while i < k:
        #     tmp = nums[0]
        #     nums[0] = nums[-1]
        #     j = 1
        #     while j < len(nums):
        #         tmp2 = nums[j]
        #         nums[j] = tmp
        #         tmp = tmp2
        #         j += 1
        #     i += 1

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
