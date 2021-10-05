import unittest
from binary_search import Solution

class TestBinarySearch(unittest.TestCase):

    def init_solution(self):
        return Solution()

    def test_simple_search(self):
        solution = self.init_solution()
        nums     = [i for i in range(11)]
        self.assertEqual(solution.search(nums,1),1)

    def test_simple_search_no_elem(self):
        solution = self.init_solution()
        nums = [i for i in range(11)]
        self.assertEqual(solution.search(nums, 11), -1)

    def test_not_in_nums(self):
        solution = self.init_solution()
        nums = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(solution.search(nums, 2), -1)
