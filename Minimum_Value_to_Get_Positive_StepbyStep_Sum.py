class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        val=psum=0
        arr=[]
        for num in nums:
            psum+=num
            arr.append(psum)
        if min(arr) >=1:
            return 1
        else: 
            return abs(min(arr))+1
