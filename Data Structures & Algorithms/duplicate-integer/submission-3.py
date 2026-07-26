class Solution(object):
    def hasDuplicate(self, nums):  
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False