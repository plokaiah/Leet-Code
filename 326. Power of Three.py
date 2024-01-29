class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        while n>=3:
            n=n/3
        return n==1
