class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        ans_list = []

        for num in nums:
            res[num] += 1
        sorted_data = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_data.keys())[:k]
            
