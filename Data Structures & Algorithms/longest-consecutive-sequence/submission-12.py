class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        longest = 1
        curr = 1
        for i in range(n-1):
            if nums[i+1] == nums[i] + 1:
                curr += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                curr=1
            longest = max(curr,longest)
        return longest
