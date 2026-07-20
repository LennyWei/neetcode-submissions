class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        easy way is to do using division

        first make a list that's n long that contains everything producted, then go through nums and divide.
        
        without division, however, becomes much harder.

        make a prefix and suffix list, build them seperately

        [1,2,4,6]
        prefix:
        [1,1,2,8]

        suffix:
        [48,24,6,1]
        '''
        

        # make prefix
        prefix = [1] * len(nums)

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = [1] * len(nums)

        for j in reversed(range(0, len(suffix)-1)):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        ret = [67] * len(nums)

        for k in range(len(nums)):
            ret[k] = prefix[k] * suffix[k]
        
        return ret

