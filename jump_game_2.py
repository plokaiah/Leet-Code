class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n < 2:
            return 0
        curr_int=nums[0]
        next_int=nums[0]
        jumps=1
        for i in range(1,n):
            next_int=max(next_int,i+nums[i])
            if i==curr_int and i!=n-1:
                curr_int=next_int
                jumps+=1
        return jumps
