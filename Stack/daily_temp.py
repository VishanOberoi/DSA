class Solution:
    def daily_temp(self, temp):
        res = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and (temp[i] > temp[stack[-1]]):
                top_of_stack_idx = stack.pop()
                res[i] = i - top_of_stack_idx
            stack.append(i)
        return res
    
