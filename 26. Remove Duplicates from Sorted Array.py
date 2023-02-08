class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        insert = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:

                nums[insert] = nums[i]
                insert = insert + 1

        return insert
