from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:


            counts[num] +=1
        sorted_keys = sorted(counts, key=counts.get, reverse=False)
        return sorted_keys[len(sorted_keys)-k:len(sorted_keys)]
        