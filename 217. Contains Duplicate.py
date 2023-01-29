class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        found = False
        checked = set()
        for i in range(len(nums)):
            if nums[i] in checked:
                found = True
            checked.add(nums[i])
            
        return found
    
