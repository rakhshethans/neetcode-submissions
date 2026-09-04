class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a frequency dictionary to track the frequency of characters
        # the most frequent character should be the repeating character
        # if the total num of other characters is k, then fine

        frequencyDict = dict()

        # use a variable sliding window
        # it grows while the number of non-majority characters in frequencyDict <= k or current char is a majority
        # it shrinks if the num of non-majority characters in frequencyDict > k, until this is true

        left = 0
        right = 0
        maxLength = 0
        maxFreq = 0
        maxFreqChar = ""

        while right < len(s):

            #.get(), if there is no s[right] key, then it will return 0
            # useful if its the first time we are seeing a character
            frequencyDict[s[right]] = frequencyDict.get(s[right], 0) + 1
            
            # check if it is the max character now
            maxFreq = max(maxFreq, frequencyDict[s[right]])

            length = right - left + 1
            # if the number of non majority chars is now greater than k, the substring is invalid so we must shrink
            while length - maxFreq > k:
                frequencyDict[s[left]] -= 1
                left += 1
                length -= 1
            
            maxLength = max(length, maxLength)

            right += 1  
        
        return maxLength




                        
                        

                