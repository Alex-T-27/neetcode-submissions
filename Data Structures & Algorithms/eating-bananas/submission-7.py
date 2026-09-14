class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            k = (l+r)//2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas/k) 
            if hours > h:
                l = k + 1
            else:
                r = k - 1
        return l