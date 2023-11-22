class Solution:
    def firstUniqChar(self, s: str) -> int:
        hp={}
        i=0
        for letter in s:
            if letter not in hp:
                hp[letter]=1
            else:
                hp[letter]+=1
            
            while s[i] in hp and hp[s[i]]>1:
                i+=1
                if i==len(s):
                    return -1
        return i
