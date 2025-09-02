from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [x[0] for x in matrix]
        array_num = self.closest_search(nums, target)
        location = True if self.binarySearch(matrix[array_num], target) != -1 else False

        return location
    
    def closest_search(self, nums: List[int], target: int) -> int:
        length = len(nums) # 2
        halfway = length // 2 # 1
        block_size = -(halfway // -2) # 1
        for i in range(halfway+1):
            if halfway == length:
                continue

            elif nums[halfway -1] <= target and nums[halfway] > target:
                return halfway - 1

            elif nums[halfway] > target:
                halfway -= block_size

            elif nums[halfway] < target:
                halfway += block_size


            block_size = -(block_size // -2)

        else:
            if halfway == length:
                halfway -= 1

            return halfway
    
    def binarySearch(self, nums: List[int], target: int) -> int:
        length = len(nums)
        halfway = length // 2
        block_size = -(halfway // -2)
        for i in range(halfway+1):
            if halfway >= length:
                continue
            if nums[halfway] == target:
                return halfway
            elif nums[halfway] > target:
                halfway -= block_size
            elif nums[halfway] < target:
                halfway += block_size


            block_size = -(block_size // -2)

        else:
            return -1
