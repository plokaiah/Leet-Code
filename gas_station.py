class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        start = 0
        res = 0
        for i in range(n):
            res = res - cost[i] + gas[i]
            if res < 0:
                start = i + 1
                res = 0
        return start
