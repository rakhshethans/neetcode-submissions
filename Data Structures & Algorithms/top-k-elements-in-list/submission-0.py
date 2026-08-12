class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = {}
        for num in nums:
            if num not in frequencyDict:
                frequencyDict[num] = 1
            else:
                frequencyDict[num] += 1
            
        # now we have a dictionary showing the frequency of every number
        # use bucket sort to group numbers by frequency

        buckets = [[] for _ in range(len(nums) + 1)] ## check how this works    
        for numFrequency in frequencyDict:
            buckets[frequencyDict[numFrequency]].append(numFrequency)
        
        # bucket sorted
        # scan backwards, to find k most frequent

        frequents = []
       

        for i in range(len(nums), 0, -1):
            bucket = buckets[i]
            for num in bucket:
                frequents.append(num)
                if len(frequents) == k:
                    return frequents
    
