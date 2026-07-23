class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        check_list = []
        for num in nums: 
            if (num not in check_list): 
                check_list.append(num)
            else:
                return True
        
        return False

