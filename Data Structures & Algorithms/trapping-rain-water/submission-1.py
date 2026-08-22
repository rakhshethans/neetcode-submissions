class Solution:
    def trap(self, height: List[int]) -> int:
        # for each bar, consider the tallest amount of water that can be stored there
        # that is bounded by the tallest bar to the left of it and the tallest bar to the right of ti
        # the height of the bar would be the minimum of the highest on the and the highest on the right, minus the bar's height
        # if there is no bar on the left that is at least taller AND right that is at least taller than the current bar, it cannot hold water above it.

        # we use 2 pointer to find the highest on the left and right
        # solution should be O(n) time and space

        # as we gradually find the highest on the left and right, we only move the limiting pointer inwards
        # as we keep track of maximum left and right height, they will only change if there is a bar higher on the right (for left pointer) or left (for right pointer). 
        # this means that for every bar, we can calculate the height of water above it as we move forwards
        # we add that to a running total of the volume
        # we only calculate this if we are going to move one of the pointers inwards.


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
        
        return volume

