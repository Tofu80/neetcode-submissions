import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(s.lower().split())
        normalStr = re.sub(r"[^a-zA-Z0-9]", "", text)

        i = 0
        j = len(normalStr) - 1

        while (i < j):
            if (normalStr[i] != normalStr[j]):
                return False
            i += 1
            j -= 1
        
        return True