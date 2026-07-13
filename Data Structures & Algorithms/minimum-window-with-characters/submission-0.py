class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # indices for our window
        answer = [0, 0]
        length = float("inf")
        
        # hashmap for t and our window
        chars, window = {}, {}
        
        # EDGE CASE: empty t
        if t == "":
            return ""

        # get the chars we need from t
        for char in t:
            chars[char] = chars.get(char, 0) + 1

        have = 0 # the chars we found
        need = len(chars) # the chars we need to find

        left = 0
        for right in range(len(s)):
            curr = s[right]
            window[curr] = window.get(curr, 0) + 1

            # found a char we need
            if curr in chars and window[curr] == chars[curr]:
                have += 1

            # found all chars we need
            while have == need:
                # find the smallest length
                if (right - left + 1) < length:
                    answer = [left, right]
                    length = right - left + 1
                
                # update the count of the char we removed
                window[s[left]] -= 1

                # if we took out a char we needed
                if s[left] in chars and window[s[left]] < chars[s[left]]:
                    have -= 1

                # shrink the window
                left += 1

        left, right = answer
        if length == float("inf"):
            return ""
        else:
            return s[left:right+1]