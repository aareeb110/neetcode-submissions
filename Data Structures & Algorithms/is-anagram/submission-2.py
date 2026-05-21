class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count_s = {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            count_s[c] = count_s.get(c, 0) - 1
        return all(v == 0 for v in count_s.values())