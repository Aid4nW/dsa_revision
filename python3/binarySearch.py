from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        halfway = length // 2 # 1
        block_size = -(halfway // -2) # 1
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

