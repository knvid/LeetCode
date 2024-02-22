class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        for i in nums: 
            count[i] += 1
            
        for key, value in count.items(): 
            if value == 1:
                return key