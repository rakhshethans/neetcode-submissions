class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # go forwads through the array,
        # pop temps if they are decreasing
        # if a temp is larger than top, pop top
        # repeat for all nums in stack that are smaller
        # not O(n) because don't need to do it every time
        # store indicies in the stack not temperature because need to know how many days until current temp'

        tempStack = [0]
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if i == 0:
                tempStack.append(i)
            else:
                while temperatures[i] > temperatures[tempStack[-1]]:
                    previousIndex = tempStack.pop()
                    daysUntil = i - previousIndex
                    result[previousIndex] = daysUntil
                    if len(tempStack) == 0:
                        break


                tempStack.append(i)  

        
        return result
                
