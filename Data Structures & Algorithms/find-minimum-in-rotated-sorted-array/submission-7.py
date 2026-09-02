class Solution:
    def findMin(self, nums: List[int]) -> int:
        # input is a rotated sorted array
        # to find minimum, have to find the first element in the array
        # the previous element will be the largest
        # look at middle then look at the first and last element of the array
        # if its more than the first and more than the last, then it has wrapped around -> the first element is to the right
        # if its is less than the first and less than the last, it has not wrapped around -> the first element is to the left

        first = 0
        last = len(nums)-1


        while first < last:
            middle = (first + last) // 2
            if nums[middle] > nums[last]:
                # min element is to the right
                # move to the right
                first = middle + 1
            elif nums[middle] < nums[last]:
                # min element is to the left
                last = middle # because the current number could be minimum as well

        if first == last:
            return nums[first]
