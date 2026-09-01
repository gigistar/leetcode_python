class Solution(object):
    def twoSum(self, nums, target):
        #num=[]
        #target_objective = target
        

        for i in range(len(nums)):
            first_number=nums[i]
            for a in range(len(nums)):
                if nums[i]+nums[a]==target and i!=a:
                    return i,a
           




        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        