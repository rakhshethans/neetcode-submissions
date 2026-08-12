class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if 2 strings are an anagram, their alphabetically ordered hash map will be the same.
        newListDict = {}
        for string in strs:
            stringList = sorted(string)
            stringNew = ""
            for char in stringList:
                stringNew += char
            # now the string is alphabetical

            if stringNew not in newListDict: 
                newListDict.update({stringNew : [string]})
            else:
                newListDict[stringNew].append(string)
            
        subLists = []

        for string in newListDict:
            subLists.append(newListDict[string])
        
        return subLists


        