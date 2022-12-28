import itertools
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # My Solution
        """
        sum = 0
        sol=[]
        for num in nums:
            sum+=num
            sol.append(sum)
        return sol
        """

        # Better Solution
        return list(itertools.accumulate(nums))
