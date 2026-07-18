class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash = {}
        thash = {}

        for ch in s:
            shash[ch] = shash.get(ch, 0) + 1 
        for ch in t:
            thash[ch] = thash.get(ch, 0) + 1 
        
        return thash == shash