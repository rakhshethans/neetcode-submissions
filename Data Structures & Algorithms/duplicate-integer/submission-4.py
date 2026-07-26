class Solution(object):
    def hasDuplicate(self, nums):  
        # numSet = set()
        # for num in nums:
        #     if num in numSet:
        #         return True
        #     else:
        #         numSet.add(num)
        # return False

        numsSet = set(nums)
        # if the length of numsSet is smaller, duplicates have been removed.
        if len(numsSet) < len(nums):
            return True
        return False