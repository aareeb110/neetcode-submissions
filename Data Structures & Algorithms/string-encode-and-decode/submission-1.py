class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            encoded_str = str(len(s)) + "#" + s
            ans += encoded_str
        print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i != len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            count = int(count)
            ans.append(s[i + 1:i + 1 + count])
            i += count + 1
        return ans