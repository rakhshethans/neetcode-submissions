class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ###
        # # mistakes:
        # #   1) forgot to sort nums
        # #   2) didn't realise that if whole thing is consecutive sequence, else statement will never be reached
        # #   -> sequence will never get added to the dictionary
        # #   3) didn't account for the list being empty
        # #   4) errors with old solution : 
        # #     a) sorted array first, which has time complexity of O(nlogn) but that wasn't allowed by the question.
        # #     b) a list is only saved when it breaks before the end of the sequence, if it doesn't it isn't saved.
        # #     c) New solution is O(n) time and O(n) space
        
        
        # # use a set to store all of the numbers
        # # use a dictionary, every number in the dictionary is a number in nums
        # # 1) sort all the numbers
        # # 2) iterate through nums, check if current num is one more than previous num
        # # 3) if it is, then add it to current consecutiveNums list.
        # # 4) if it isn't, add it to dictionary, its length is the key.
        # # 5) if it is equal, we ignore and check the next one
        # # 6) reset the consecutiveNums list.
        # # 7) at the end, find the max in the dictionary
        # # this is the result
        
        # nums.sort()

        # consecutiveSequences = dict()
        # # check that nums actually has numbers
        # if len(nums) > 0:
        #     currentSequence = [nums[0]]
        # else:
        #     return 0
        # sequenceLength = 1
        # wholeListIsSequence = True

        # for i in range(1, len(nums)):
        #     if (nums[i] - nums[i-1]) == 1:
        #         currentSequence.append(nums[i])
        #         sequenceLength += 1
        #     elif nums[i] == nums[i-1]:
        #         continue
        #     else:
        #         wholeListIsSequence = False # if this is ever reached, its not possible for the whole list to be a sequence
        #         consecutiveSequences[sequenceLength] = currentSequence
        #         currentSequence = [nums[i]]
        #         sequenceLength = 1
            
        # if wholeListIsSequence:
        #     longestSequence = sequenceLength
        # else:
        #     longestSequence = max(consecutiveSequences)
        # return longestSequence


        #################################################
        # new method

        # for each number, check if there is one number greater than it.
        # keep going until you can't find any numbers greater than it
        # store numbers in a set for O(1) lookup time.

        # first, add all numbers to a set

        numsSet = set(nums)
        
        # then, go through each number in the set,
        # to find the start of the set there must not be a number that is lower
        # could be multiple starts

        longestLength = 0
        for num in numsSet:
            if (num - 1) not in numsSet:
                # nums[i] is a start
                currentNum = num
                currentLength = 1

                while currentNum + 1 in numsSet:
                    currentNum += 1
                    currentLength += 1
                
                longestLength = max(currentLength, longestLength)
        
        return longestLength

            
