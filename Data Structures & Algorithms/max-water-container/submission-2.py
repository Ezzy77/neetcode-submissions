class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVal = 0

        for i in range(len(heights)):
            area = 0
            for j in range(i + 1, len(heights)):
                maxVal = max(maxVal, min(heights[i], heights[j]) * (j - i))
        return maxVal
        