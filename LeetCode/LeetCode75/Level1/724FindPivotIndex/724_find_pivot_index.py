from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left  = 0
        sum_right = sum(nums[1:])

        for index in range(0,len(nums)-1):
            num = nums[index]
            if sum_left == sum_right:
                return index
            sum_left  += num
            sum_right -= nums[index+1]
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,-1,0,1,1,0]
    # nums = [1,7,3,6,5,6]
    print(sol.pivotIndex(nums))
