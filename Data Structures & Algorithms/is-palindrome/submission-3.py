class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # check if the char is alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            
            # compare them as lowercase letters
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
    
    def alphaNum(self, c: char) -> bool:
        # ord(): gives the UNICODE number value
        return (ord('A') <= ord(c) <= ord('Z') or # uppercase
                ord('a') <= ord(c) <= ord('z') or # lowercase
                ord('0') <= ord(c) <= ord('9')) # numeric