class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for s in tokens:
            if s not in "+-*/":
                nums.append(int(s))
            else:
                b = nums.pop()
                a = nums.pop()

                if s == '+':
                    nums.append(a+b)
                elif s == '-':
                    nums.append(a-b)
                elif s == '*':
                    nums.append(a*b)
                elif s == '/':
                    nums.append(int(a/b))
        return nums[0]