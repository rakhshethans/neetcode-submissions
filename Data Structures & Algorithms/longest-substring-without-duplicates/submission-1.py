class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # check for duplicate characters -> use a set
        # variable sliding window
        # extend right until there is a duplicate character
        # once there is, shrink from the left until there are no duplicates
        # store max length of set

        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1

        left = 0
        right = left
        uniqueCharacters = set()
        maxLength = 0
        while right < len(s):
            while s[right] in uniqueCharacters and left < right:
                uniqueCharacters.remove(s[left])
                left += 1
            
            uniqueCharacters.add(s[right])
            right += 1
            maxLength = max(maxLength, len(uniqueCharacters))


        return maxLength