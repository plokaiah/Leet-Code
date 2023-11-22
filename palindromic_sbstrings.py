
//by using two pointer:
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        def pal(s,l,r):
            count = 0
            
            while l>=0 and r<len(s) and s[l] == s[r]:
                count +=1
                l -=1
                r +=1
            return count
        
        for i in range(len(s)):
            count += pal(s,i,i) # for odd palindroms
            count += pal(s,i,i+1) #for even palindroms
            
        return count

//by using sliding window:
class Solution:
    def isPalindrome(self, word):
        if word == word[::-1]:
            return True
        return False

    def countSubstrings(self, s: str) -> int:
        ans = 0
        L = 0
        while L <= len(s) - 1:
            for R in range(L + 1, len(s) + 1):
                ans += self.isPalindrome(s[L:R])
            L += 1
        return ans
