from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_index = -1
        sum_left  = 0
        sum_right = sum(nums[1:])
        if sum_left == sum_right:
                pivot_index = 0
                return pivot_index
        for index in range(1,len(nums)):
            print(index)
            value=nums[index]
            sum_left  += nums[index-1]
            sum_right -= value
            if sum_left == sum_right:
                pivot_index = index
                return index
        return pivot_index


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,-1,0,1,1,0]
    # nums = [1,7,3,6,5,6]
    print(sol.pivotIndex(nums))
