from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalanswer = defaultdict(list)
        for wrd in strs:
            key = tuple(sorted(wrd))
            finalanswer[key].append(wrd)

        return list(finalanswer.values())