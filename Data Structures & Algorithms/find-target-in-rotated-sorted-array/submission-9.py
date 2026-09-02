class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        while first <= last:
            middle = (first + last) // 2
            if nums[middle] == target:
                return middle

            if nums[middle] <= nums[last]:
                # list starts in left sublist or at current index
                if target > nums[middle] and target <= nums[last]:
                    first = middle + 1
                else:
                    last = middle - 1
            
            else:
                # list starts in right sublist
                if target >= nums[first] and target < nums[middle]:
                    last = middle - 1
                else:
                    first = middle + 1

        return -1
