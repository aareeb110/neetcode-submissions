class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        start = 0
        max_len = 0
        max_freq = 0

        for end in range(len(s)):
            right_char = s[end]
            counts[right_char] = counts.get(right_char, 0) + 1
            max_freq = max(max_freq, counts[right_char])

            window_size = end - start + 1
            if window_size - max_freq > k:
                left_char = s[start]
                counts[left_char] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len