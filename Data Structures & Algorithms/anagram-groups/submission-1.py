class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in hashmap:
                hashmap[sorted_str] = []
            hashmap[sorted_str].append(string)
        return list(hashmap.values())
