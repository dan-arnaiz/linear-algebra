class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        mp = Counter(nums)
        
        count = 0
        for t in mp.values():
            while t >= 2 and len(mp) > 1:
                count += 1
                t -= 2
            count += t // 3
            t %= 3
            if t == 1:
                return -1
                
        return count