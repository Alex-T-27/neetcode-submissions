class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] * n
        prefix[0] = nums[0]

        suffix = [1] * n
        suffix[n-1] = nums[n-1]

        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i+1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        res = [1] * n

        res[0] = suffix[1]
        res[n-1] = prefix[n-2]

        for i in range(1, n-1, 1):
            res[i] = suffix[i+1] * prefix[i-1]
        
        return res
        

