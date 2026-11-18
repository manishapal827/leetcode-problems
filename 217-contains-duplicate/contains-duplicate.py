class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
        #two ways
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False