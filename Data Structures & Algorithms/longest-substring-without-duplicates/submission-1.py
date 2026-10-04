class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        left = 0
        result = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[left])
                left += 1
            window.add(s[r])
            result = max(result, r - left + 1)
        return result
        