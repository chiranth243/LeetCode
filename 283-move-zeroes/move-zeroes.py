class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lastzero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastzero], nums[i] = nums[i], nums[lastzero]
                lastzero += 1
        