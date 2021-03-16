class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1+nums2       
        num3.sort()
        idx= (len(num3)-1)//2
        if len(num3)%2 == 0:
            return (num3[idx] + num3[idx+1])/2
        else:
            return num3[idx]