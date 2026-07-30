class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        for num in nums1:
            map1[num] = 1 + map1.get(num, 0)

        k = 0
        for num in nums2:
            if num in map1 and map1[num] > 0:
                nums1[k] = num
                map1[num] -= 1
                k += 1
        return nums1[0 : k]



                