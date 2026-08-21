class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n) time so you only want to search the array once
        # can't sort
        # two pointers, one at start and one at end
        # loop while i < j
        # go inwards
        # if heights[i] > largestLeftHeight replace it
        # if heights[j] > largestRightHeight replace it


        # i = 0
        # j = len(heights) - 1
        # largestLeftHeight = heights[i]
        # largestRightHeight = heights[j]

        # while i < j:
        #     if heights[i] > largestLeftHeight:
        #         largestLeftHeight = heights[i]
        #     if heights[j] > largestRightHeight:
        #         largestRightHeight = heights[j]
            
        #     i += 1
        #     j -= 1
        
        # return (largestLeftHeight + largestRightHeight)

        #####################

        # doesn't work because doesn't account for bars on the same side
        # also want to return container area not height sum

        #####################

        # use 2 pointer algorithm
        # move the height container that has the smallest height inwards
        # we do this because we want to maximise both width and height
        # meaning its a greedy algorithm

        largestArea = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[j], heights[i])

            if area > largestArea:
                largestArea = area
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        

        return largestArea






