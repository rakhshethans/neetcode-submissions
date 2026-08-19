class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        newS = ""
        for letter in s:
            newS = newS + letter 
        reverseS = newS[::-1]
        if newS == reverseS:
            return True
        else:
            return False