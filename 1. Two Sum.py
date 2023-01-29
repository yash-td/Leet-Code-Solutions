class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        checked = {}

        for i,ele in enumerate(nums):
            if (target-ele) in checked:
                return [checked[target-ele],i]
            
            checked[ele] = i
        
        return
