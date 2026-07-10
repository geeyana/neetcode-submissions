class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = answer = 0
        window = set()

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            else:
                window.add(s[right])
            answer = max(len(window), answer)
        
        return answer