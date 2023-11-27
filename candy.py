class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if ratings==None or len(ratings)==0: return 0
        arr=[1 for _ in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                arr[i]=arr[i-1]+1
        s=arr[len(ratings)-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                if arr[i]<arr[i+1]+1:
                    arr[i]=arr[i+1]+1
            s+=arr[i]
        
        return s
