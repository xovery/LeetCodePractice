class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_a = m-1
        ptr_b = n-1
        ptr_Last = m + n - 1

        while ptr_a >=0 and ptr_b >=0 :
            if(nums1[ptr_a] > nums2[ptr_b]):
                nums1[ptr_Last] = nums1[ptr_a]
                ptr_a -= 1
            else:
                nums1[ptr_Last] = nums2[ptr_b]
                ptr_b -= 1
            ptr_Last -= 1

        while ptr_b >= 0:
            nums1[ptr_Last] = nums2[ptr_b]
            ptr_b -= 1
            ptr_Last -= 1

            



