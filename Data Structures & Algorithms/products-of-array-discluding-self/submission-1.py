class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # don't need to use recursion
        # # use prefix suffix method
        # # we use an array to store the prefix product values for every index
        # # we use an array to store the suffix product values for every index
        # # product = prefix[i] * suffix[i]

        # # prefix calculating loop
        # prefixProducts = []
        # for i in range(0, len(nums)):
        #     if i == 0: 
        #         prefixProducts.append(1)
        #     else:
        #         currentPrefix = prefixProducts[i-1] * nums[i-1]
        #         prefixProducts.append(currentPrefix)

        
        # # suffix calculating loop
        # # reverse the nums array so you can use the same logic
        # reverseNums = nums[::-1]
        # suffixProducts = []
        # for i in range(0, len(reverseNums)):
        #     if i == 0:
        #         suffixProducts.append(1)
        #     else:
        #         currentSuffix = suffixProducts[i-1] * reverseNums[i-1]
        #         suffixProducts.append(currentSuffix)
        
        # suffixProducts = suffixProducts[::-1]

        # # now calculate the product except self for every value
        # productExceptSelf = []
        # for i in range(0, len(nums)):
        #     productExceptSelf.append(prefixProducts[i] * suffixProducts[i])
        
        # return productExceptSelf



        ####################################################################

        # there is a more space efficient solution
        # instead of creating 2 extra arrays, one for the prefix and one for the suffix
        # we write the prefix values into the result array during the 1st pass of nums (where we calculate the prefixes)
        # then, during the suffix pass, we simply multiply the current prefix value with the calculated suffix to find the productExceptSelf.

        result = []

        prefixProduct = 1
        for i in range(0, len(nums)):
            if i == 0: 
                result.append(1)
            else:
                currentPrefix = prefixProduct * nums[i-1]
                result.append(currentPrefix)
                prefixProduct = currentPrefix


        # now the result array is populated with every element's prefix product
        # we do the suffix product pass now

        resultReverse = result[::-1]
        numsReverse = nums[::-1]
        suffixProduct = 1
        for i in range(0, len(numsReverse)):
            if i == 0:
                resultReverse[i] = resultReverse[i] * 1
            else:
                currentSuffix = suffixProduct * numsReverse[i-1]
                resultReverse[i] *= currentSuffix
                suffixProduct = currentSuffix
        
        finalResult = resultReverse[::-1]
        return finalResult

        
        
        