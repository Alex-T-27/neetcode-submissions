class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            sorted_text = "".join(sorted(word))
            groups[sorted_text].append(word)

            
        return list(groups.values())
            

