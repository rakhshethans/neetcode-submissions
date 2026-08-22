class Solution:
    def trap(self, height: List[int]) -> int:
        # for each bar, consider the tallest amount of water that can be stored there
        # that is bounded by the tallest bar to the left of it and the tallest bar to the right of ti
        # the height of the bar would be the minimum of the highest on the and the highest on the right, minus the bar's height
        # if there is no bar on the left that is at least taller AND right that is at least taller than the current bar, it cannot hold water above it.

        # we use 2 pointer to find the highest on the left and right
        # solution should be O(n) time and space

        # water above bar = min(leftMax, rightMax) - height
        # not sure
        # not sure

        leftMax = 0
        rightMax = 0
        volume = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] > leftMax:
                leftMax = height[i]
            if height[j] > rightMax:
                rightMax = height[j]
            
            if leftMax < rightMax:
                currentHeight = leftMax - height[i]
                volume += currentHeight
                i += 1
            else:
                currentHeight = rightMax - height[j]
                volume += currentHeight
                j -= 1
            
        # now leftMax is the tallest bar on the left half
        # rightMax is the tallest bar on the right half

        # now go through graphs from i = 1 to i = n-2 (because x = 0 and x = len(height) -1 don't count as walls)

        return volume

