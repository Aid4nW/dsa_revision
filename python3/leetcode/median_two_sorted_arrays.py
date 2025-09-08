from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_count = len(nums1) + len(nums2)
        halfway = total_count // 2 + 1 if total_count % 2 == 0 else total_count // 2 + 1
        ret_val = 0.0
        constructed_list = []
        # Count to halfway point
        for i in range(halfway):

            # Protect from empty lists, one list must not be empty on entry
            if not nums1 and not nums2:
                break
            elif not nums1 and nums2:
                constructed_list.append(nums2.pop(0))
            elif not nums2 and nums1:
                constructed_list.append(nums1.pop(0))

            # Main loop, pull in the next biggest number
            elif nums1[0] >= nums2[0]:
                constructed_list.append(nums2.pop(0))
                
            elif nums1[0] < nums2[0]:
                constructed_list.append(nums1.pop(0))
        
        if total_count % 2 == 0:
            ret_val = (constructed_list[-1] + constructed_list[-2]) / 2
        else:
            ret_val = constructed_list[-1]
        

        return ret_val