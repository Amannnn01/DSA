class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for value in strs:
            count=[0]*26

            for ch in value:
                count[ord(ch)-ord('a')]+=1

            key=tuple(count)

            if key not in d:
                d[key]=[]

            d[key].append(value)

        return list(d.values())



        



            
                

       
        