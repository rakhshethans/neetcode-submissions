class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we have 2 frequency maps one for the current window and one for t
        # we use a sliding window
        # we grow until we have a valid substring
        # we shrink to find the smallest valid substring
        # then we continue growing

        # generate frequency map for t
        tFreqMap = dict()
        needCount = 0
        for char in t:
            tFreqMap[char] = tFreqMap.get(char, 0) + 1
        needCount = len(tFreqMap)

        # sliding window
        sFreqMap = dict()
        have = 0
        left = 0
        right = 0
        minSize = float("inf")
        bestLeft = 0
        bestRight = 0
        containsValidSubString = False

        while right < len(s):
            # add current char to sFreqMap
            sFreqMap[s[right]] = sFreqMap.get(s[right], 0) + 1
            
            # check if it is a required char
            # if it is, increment have
            if s[right] in tFreqMap:
                if sFreqMap[s[right]] == tFreqMap[s[right]]:
                    have += 1
            
            # if we have a valid substring
  
            # shrink from the left until it isn't valid:
            # remove the left char from sFreqMap
            # update have var
            # increment left
   
            while have == needCount:
                containsValidSubString = True
                sFreqMap[s[left]] -= 1
                if s[left] in tFreqMap.keys() and sFreqMap[s[left]] < tFreqMap[s[left]]:
                    have -= 1

                if right - left + 1 < minSize:
                    minSize = (right - left) + 1
                    bestLeft = left
                    bestRight = right

                left += 1
            
            right += 1
    
        if containsValidSubString:
            return s[bestLeft: bestRight + 1]
        else:
            return ""