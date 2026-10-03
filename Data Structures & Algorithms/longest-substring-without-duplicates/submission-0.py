class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window
        expand() until there is a duplication
        update maxLength
        shrink() until no more duplication
        '''
        maxLength = 0
        existed = set()
        l = 0
        for r in range(len(s)):
            #shrink
            while l < r and s[r] in existed: 
                existed.remove(s[l])
                l += 1
            #expand
            existed.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength
        '''
        dry run 
        func("zxyzxyz")
        
        '''




        