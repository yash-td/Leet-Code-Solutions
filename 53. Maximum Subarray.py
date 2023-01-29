class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        currSum = 0
        for ele in nums:

            if currSum < 0:
                currSum = 0
            currSum = currSum + ele
            maxSub = max(currSum,maxSub)

        return maxSub
            
