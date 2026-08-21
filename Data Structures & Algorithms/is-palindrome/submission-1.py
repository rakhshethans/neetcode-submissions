class Solution:
    def isPalindrome(self, s: str) -> bool:
            # first remove all non numeric or alphabetic characters from string
            newS = ""
            for char in s:
                if char.isalnum():
                    newS = newS + char.lower()


            i = 0
            j = len(newS) - 1
            while i < j:
                if newS[i] == newS[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            
            return True