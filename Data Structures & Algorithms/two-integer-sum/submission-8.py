class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        for i in range(0, len(nums)):
            keys = numDict.keys()
            if nums[i] not in keys:
                numDict[nums[i]] = i
        
        keys = numDict.keys()

        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in keys:
                j  = numDict[difference]

                if i != j:
                    return [min(i, numDict[difference]), max(i, numDict[difference])]