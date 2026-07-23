class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        check_dict = {}
        for c in s:
            if c not in check_dict:
                check_dict[c] = 1
            if c in check_dict:
                check_dict[c] += 1

        check_dict_2 = {}
        for c in t:
            if c not in check_dict_2:
                check_dict_2[c] = 1
            if c in check_dict_2:
                check_dict_2[c] += 1
        if check_dict == check_dict_2:
            return True
        return False

            
