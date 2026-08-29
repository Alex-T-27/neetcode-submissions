class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(filter(str.isalnum, s))
        final = cleaned_s.lower()
        n = len(final)
        left = 0 
        right = n-1
        while left < right:
            if final[left] != final[right]:
                return False
            left += 1
            right -= 1
        return True
        