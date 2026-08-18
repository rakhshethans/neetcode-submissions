class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # don't need to use recursion
        # use prefix suffix method
        # we use an array to store the prefix product values for every index
        # we use an array to store the suffix product values for every index
        # product = prefix[i] * suffix[i]

        # prefix calculating loop
        prefixProducts = []
        for i in range(0, len(nums)):
            if i == 0: 
                prefixProducts.append(1)
            else:
                currentPrefix = prefixProducts[i-1] * nums[i-1]
                prefixProducts.append(currentPrefix)

        
        # suffix calculating loop
        # reverse the nums array so you can use the same logic
        reverseNums = nums[::-1]
        suffixProducts = []
        for i in range(0, len(reverseNums)):
            if i == 0:
                suffixProducts.append(1)
            else:
                currentSuffix = suffixProducts[i-1] * reverseNums[i-1]
                suffixProducts.append(currentSuffix)
        
        suffixProducts = suffixProducts[::-1]

        # now calculate the product except self for every value
        productExceptSelf = []
        for i in range(0, len(nums)):
            productExceptSelf.append(prefixProducts[i] * suffixProducts[i])
        
        return productExceptSelf
        
        
        