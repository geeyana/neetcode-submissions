class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum())
        string = string.lower()

        left = 0
        right = len(string)-1

        while right > left:
            if string[right] != string[left]:
                return False
            left += 1
            right -= 1
        
        return True