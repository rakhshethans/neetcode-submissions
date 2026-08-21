class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the array is already sorted
        # use 2 pointers, 1 at start and 1 at end
        # add numbers at pointers together
        # if they = target, return first and last
        # if sum is bigger, then go back from end (to add a smaller number to first)
        # if sum is lesser, then go forward one (to add a larger number to last)

        i = 0 
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            elif sum < target:
                i += 1
            else:
                j -= 1
        
        # there should always be a valid solution, so this should never be reached
