class Solution:
    def dailyTemperatures(self, tmps: List[int]) -> List[int]:
        res = [0] * len(tmps)
        stack = [] # [temp, index]

        for i, t in enumerate(tmps):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res


            
        