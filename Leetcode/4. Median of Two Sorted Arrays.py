class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        k = len(merged)
        merged.sort()

        if k % 2 == 0:
            median = (merged[k//2 - 1] + merged[k//2]) / 2.0
        else:
            median = merged[k//2]

        return float("{:.5f}".format(median))
