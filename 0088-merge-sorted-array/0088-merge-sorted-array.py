class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        ptr1 = 0
        ptr2 = 0
        while(ptr1 < m and ptr2 < n):
            if(nums1[ptr1] < nums2[ptr2]):
                res.append(nums1[ptr1])
                ptr1 += 1
            else:
                res.append(nums2[ptr2])
                ptr2 += 1
        if(ptr1 < m):
            res += (nums1[ptr1 : m])
        if(ptr2 < n):
            res += (nums2[ptr2 : n])

        for i in range(0, len(res)):
            nums1[i] = res[i]
        