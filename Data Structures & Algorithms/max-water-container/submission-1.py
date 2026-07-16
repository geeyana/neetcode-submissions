class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we need two pointers
        l = maxArea = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r]) # get the shortest height of the two
            length = r-l # find the distance between them
            area = length * height # calculate areaa
            maxArea = max(maxArea, area) # update max

            # update one of the pointers
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea
