class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0

        while(left < right):
            length = right - left
            breadth = min(height[left], height[right])
            area = length * breadth
            maxArea = max(maxArea, area)

            if(height[left] <= height[right]):
                left += 1
            else:
                right -= 1
        return maxArea