class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i , value in enumerate(nums):
            complement=target- value

            if complement in d :
                return [d[complement], i]


            d[value]=i

       





        
        

       
        

        