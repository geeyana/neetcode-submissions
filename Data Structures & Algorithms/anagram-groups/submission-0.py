from collections import defaultdict # gives us empty lists as values  
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {(count of chars) : [anagrams with those chars]}
        sorted_anagrams = defaultdict(list)

        # pick one word in the list
        for s in strs:
            count = [0] * 26 # initialize list to 0 for each letter in the alphabet

            # pick one char in the word
            for c in s:
                index = ord(c) - ord('a') # gives us 0-25
                count[index] += 1 # add 1 for that char

            key = tuple(count) # keys in dicts must be immutable
            sorted_anagrams[key].append(s) # associate anagrams with their count of chars

        return list(sorted_anagrams.values())