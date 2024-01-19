class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left =0
        right = sum(nums)
        for index, nums in enumerate(nums):
            right-=nums
            if left==right:
                return index
            left+=nums           
        return -1
