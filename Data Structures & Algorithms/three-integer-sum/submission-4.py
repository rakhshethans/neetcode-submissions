class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # nums[i] + nums[j] = -nums[k]
        # # go through each number and search backwards from the end of the array to it
        # validTriplets = []

        # for i in range(0, len(nums)):
        #     k = len(nums) - 1
        #     for j in range(i, len(nums)):
        #         currentSum = nums[j] + nums[k]
        #         # check if -currentSum is in the nums array
        #         # if it is, then we have found a valid triplet
        #         if (-currentSum) in nums:
        #             if [nums[j], nums[k], -currentSum] not in nums or [nums[k], nums[j], -currentSum] not in nums or [-currentSum, nums[k], nums[j]] not in nums or [nums[j], -currentSum, nums[k]] not in nums:
                     
        #                 validTriplets.append([nums[j], nums[k], -currentSum])
        #         else:
        #             k -= 1
        
        # return validTriplets


        # essentially a two sum problem again
        # fix one number, then with the rest of the list, find a 2 sum that is the negative of the fixed number
        nums.sort()

        # fix i
        validTriplets = []
        for i in range(0, len(nums)):
            if nums[i] != nums[i-1] or i == 0:
                currentFixedNum = nums[i]
                j = i+1
                k = len(nums) - 1
                # we want to find a 2 sum such that nums[j] + nums[k] = -currentFixedNum
                while j < k:
                    currentSum = nums[j] + nums[k]
                    if currentSum == -currentFixedNum:
                        # we have found a triplet
                        validTriplets.append([nums[j], nums[k], currentFixedNum])
                        oldJ = nums[j]
                        oldK = nums[k]
                        j += 1
                        k -= 1
                        while j < k and nums[j] == oldJ:
                            j += 1
                        while j < k and nums[k] == oldK:
                            k -= 1

                    elif currentSum < -currentFixedNum:
                        # we want a bigger currentSum
                        j += 1
                    else:
                        k -= 1
                            
        return validTriplets