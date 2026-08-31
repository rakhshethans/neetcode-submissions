class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heightsStack = []
        greatestArea = 0
        for i in range(len(heights)):
            start = i
            while heightsStack and heights[i] < heightsStack[-1][0]:
                currentTop = heightsStack.pop()

                height = currentTop[0]
                startIndex = currentTop[1]

                base = i - startIndex
                currentArea = base * height
                greatestArea = max(greatestArea, currentArea)

                start = startIndex
            
            heightsStack.append((heights[i], start))

        for height, startIndex in heightsStack:
            base = len(heights) - startIndex
            currentArea = base * height
            greatestArea = max(greatestArea, currentArea)
        
        return greatestArea

