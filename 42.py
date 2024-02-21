class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        for i in range(1,len(height)-1):
            water += min(max(height[0:i+1]), max(height[i:len(height)])) - height[i]
        return water

test = Solution()
arr = [4,2,0,3,2,5]

print(test.trap(height=arr))