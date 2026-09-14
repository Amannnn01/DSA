class Solution(object):
    def containsDuplicate(self, nums):
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1

        for value in d.values():
            if value != 1:
                return True

            
        
        return False
    



        


        
        
        
       
        

        