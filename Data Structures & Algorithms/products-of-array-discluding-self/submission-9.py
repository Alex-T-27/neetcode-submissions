class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        pre, pos = 1, 1 
        
        res = [1] * n

        for i in range(n-1):
            pre *= nums[i]
            res[i+1] = pre

        for j in range(n-1, -1, -1):
            res[j] *= pos
            pos *= nums[j]

        return res

