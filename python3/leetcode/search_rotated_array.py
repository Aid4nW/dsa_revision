from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = low + ((high-low) // 2)
            print(f"High: {high}, Low: {low}, Mid: {mid}")
            
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[low]:
                # Left half is sorted
                if target >= nums[low] and target < nums[mid]:
                    # Search left half
                    high = mid - 1                   
                else:
                     # Search right half
                    low = mid + 1
            else:
                # Right half is sorted
                if target > nums[mid] and target <= nums[high]:
                    # Search right half
                    low = mid + 1
                else:
                    # Search left half
                    high = mid - 1
                    

        return -1