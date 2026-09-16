class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1 = {}
        for s1 in s:
            if s1 not in res1:
                res1[s1] = 1
            else:
                res1[s1] += 1
        res2 = {}
        for s2 in t:
            if s2 not in res2:
                res2[s2] = 1
            else:
                res2[s2] += 1
        if res1 == res2:
            return True
        return False 