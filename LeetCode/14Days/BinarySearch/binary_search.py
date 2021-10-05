from typing import List
from unittest.main import main


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        middle = (first+last)//2
        
        if (target<nums[first]) or (target>nums[last]):
            return -1

        while first <= last:
            self.debug_messages(first, middle, last, nums, target)
            if nums[middle] == target:
                return middle
            if nums[first] == target:
                return first
            if nums[last] == target:
                return last
            if ((first == middle) and nums[middle] != target) or ((last == middle) and nums[middle] != target):
                return -1
            else:
                if nums[middle] < target:
                    first = middle
                    middle = (first+last)//2
                if nums[middle] > target:
                    last = middle
                    middle = (first+last)//2
        return -1

    def debug_messages(self, first, mid, last, nums, target):
        print("\n", "="*50)
        print(
            f"The Given list is:\n{nums}\nFirst: {first}\nMiddle: {mid}\nLast: {last}\nTarget:{target}")
        print("="*50, "\n")


if __name__ == "__main__":
    # nums = [num for num in range(11)]
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    solution = Solution()
    # for target in range(-20,21):
    print(f"Target `{target}` found at index: {solution.search(nums,target)}")
