class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newnums = nums1 + nums2
        newnums.sort()

        mid = int(len(newnums) / 2)
        if len(newnums) % 2  == 0:
                return float((newnums[mid] + newnums[mid-1] ) / 2)
            
        else: 
                return float(newnums[mid])

        
        