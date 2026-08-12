class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # if 2 strings are an anagram, their alphabetically ordered hash map will be the same.
        # newListDict = {}
        # for string in strs:
        #     stringList = sorted(string)
        #     stringNew = ""
        #     for char in stringList:
        #         stringNew += char
        #     # now the string is alphabetical

        #     if stringNew not in newListDict: 
        #         newListDict.update({stringNew : [string]})
        #     else:
        #         newListDict[stringNew].append(string)
            
        # subLists = []

        # for string in newListDict:
        #     subLists.append(newListDict[string])
        
        # return subLists



        ################

        # more efficient approach
        # use letter frequency instead.

        # for each word, find its array of 26 letters, finding its frequency
        # have an dictionary for letter frequency arrays, if its already there, add the string to the sublist
        # otherwise create a new sublist
        # create and return a final list using the dictionary

        stringDict = {}

        for string in strs:
            letterFrequency = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                letterFrequency[index] += 1
            
            letterFrequency = tuple(letterFrequency)

            if letterFrequency not in stringDict:
                stringDict[letterFrequency] = [string]
            else:
                stringDict[letterFrequency].append(string)
            
        
        return list(stringDict.values())




        