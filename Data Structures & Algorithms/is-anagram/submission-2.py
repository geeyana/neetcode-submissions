from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        shash = defaultdict(int)
        thash = defaultdict(int)

        for ch in s:
            shash[ch] += 1
        for ch in t:
            thash[ch] += 1

        return shash == thash