class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        lmax, rmax = 0, 0

        water = 0

        while l < r:
            if (height[l] <= height[r]):

                if lmax <= height[l]:
                    lmax = height[l]
                else:
                    water += lmax - height[l]

                l += 1

            else:

                if rmax <= height[r]:
                    rmax = height[r]
                else:
                    water += rmax - height[r]

                r -= 1
        return water

        
