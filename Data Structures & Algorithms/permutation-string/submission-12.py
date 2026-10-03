class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        if len(s2) < len(s1):
            return False

        for s in s1:
            freq1[s] += 1
        for i in range(len(s1)):
            freq2[s2[i]] += 1
        if freq2 == freq1:
            return True


        r = len(s1) - 1

        while r <= len(s2)-2:
            if freq2 == freq1:
                return True
            freq2[s2[l]] -= 1
            if freq2[s2[l]] == 0:
                del freq2[s2[l]]
            r += 1
            l += 1
            freq2[s2[r]] += 1
            if freq2 == freq1:
                return True

        return False 
 
        


        '''
        check freq cua nhung ki tu trong s1
        luu vo hashmap freq1

        cho mot cai fixedsize window trong, size = len(s1)
        r += 1
        l += 1
        freq2 cua s2[r] += 1
        freq2 [s2[l]] -= 1
        neu freq1 == freq2 => true
        return false

        '''