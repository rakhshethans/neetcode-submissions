class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check middle num
        # if target, return index
        # if less than target, discard left half of list and repeat
        # if more than target, discard right half of list and repeat

        first = 0
        last = len(nums) 

        
        while first < last:
            middle = (first + last) // 2
            if nums[middle] == target:
                return middle
            else:
                if nums[middle] < target:
                    # we want the right sublist
                    first = middle+1
                else:
                    # we want the left sublist
                    last = middle
        
        return -1