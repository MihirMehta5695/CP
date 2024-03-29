// class Solution:
//     def search(self, nums: List[int], target: int) -> int:
//         int low = 0;
//         int high = len(nums)-1;
//         while(low <= high):
//             mid = (low + high)//2
//             if (nums[mid] == target):
//                 return mid
//             if(target < nums[mid]):
//                 high = mid-1
//             else:
//                 low = mid+1
//         return -1
using std::vector;
class Solution
{
public:
    int search(std::vector<int> &nums, int target)
    {
        int low = 0;
        int high = nums.size() - 1;
        int mid = 0;
        while (low <= high)
        {
            mid = (low + high) / 2;
            if (nums[mid] == target)
            {
                return mid;
            }
            if (target < nums[mid])
            {
                high = mid - 1;
            }
            else
            {
                low = mid + 1;
            }
        }
        return -1;
    }
};